import Cocoa
import SwiftUI

class OverlayWindow: NSPanel {
    var overlayView: OverlayContentView!
    var trackingTimer: Timer?
    
    init() {
        // Start with a default frame, will be updated
        let defaultFrame = NSRect(x: 0, y: 0, width: 1920, height: 1080)
        
        super.init(
            contentRect: defaultFrame,
            styleMask: [.borderless, .nonactivatingPanel],
            backing: .buffered,
            defer: false
        )
        
        // Window configuration for overlay
        self.isFloatingPanel = true
        self.level = .floating
        self.collectionBehavior = [.canJoinAllSpaces, .fullScreenAuxiliary]
        self.isOpaque = false
        self.backgroundColor = .clear
        self.hasShadow = false
        self.ignoresMouseEvents = true  // Click-through
        
        // Create the SwiftUI view
        overlayView = OverlayContentView()
        let hostingView = NSHostingView(rootView: OverlayRootView(content: overlayView))
        self.contentView = hostingView
        
        // Start tracking Hearthstone window
        startTrackingHearthstone()
        
        print("[OverlayWindow] Initialized, tracking Hearthstone window...")
    }
    
    func startTrackingHearthstone() {
        // Initial position
        updatePositionToHearthstone()
        
        // Poll every 0.5 seconds for window position changes
        trackingTimer = Timer.scheduledTimer(withTimeInterval: 0.5, repeats: true) { [weak self] _ in
            self?.updatePositionToHearthstone()
        }
    }
    
    func stopTracking() {
        trackingTimer?.invalidate()
        trackingTimer = nil
    }
    
    func updatePositionToHearthstone() {
        guard let hsFrame = findHearthstoneWindow() else {
            // Hearthstone not found, hide overlay
            self.orderOut(nil)
            return
        }
        
        // Convert from screen coordinates (top-left origin) to Cocoa (bottom-left origin)
        guard let screen = NSScreen.main else { return }
        let screenHeight = screen.frame.height
        
        let cocoaFrame = NSRect(
            x: hsFrame.origin.x,
            y: screenHeight - hsFrame.origin.y - hsFrame.height,
            width: hsFrame.width,
            height: hsFrame.height
        )
        
        // Update frame if changed
        if self.frame != cocoaFrame {
            self.setFrame(cocoaFrame, display: true)
            (self.contentView as? NSHostingView<OverlayRootView>)?.frame = NSRect(origin: .zero, size: cocoaFrame.size)
            print("[OverlayWindow] Positioned on Hearthstone: \(cocoaFrame)")
        }
        
        // Make sure we're visible
        if !self.isVisible {
            self.orderFrontRegardless()
        }
    }
    
    func findHearthstoneWindow() -> CGRect? {
        // Get list of all windows
        let options: CGWindowListOption = [.optionOnScreenOnly, .excludeDesktopElements]
        guard let windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID) as? [[String: Any]] else {
            return nil
        }
        
        // Find Hearthstone window
        for window in windowList {
            guard let ownerName = window[kCGWindowOwnerName as String] as? String,
                  ownerName == "Hearthstone",
                  let bounds = window[kCGWindowBounds as String] as? [String: CGFloat] else {
                continue
            }
            
            let x = bounds["X"] ?? 0
            let y = bounds["Y"] ?? 0
            let width = bounds["Width"] ?? 0
            let height = bounds["Height"] ?? 0
            
            // Skip very small windows (like menu bar items)
            if width > 400 && height > 300 {
                return CGRect(x: x, y: y, width: width, height: height)
            }
        }
        
        return nil
    }
}

// Observable class for overlay state
class OverlayContentView: ObservableObject {
    @Published var arrowStart: CGPoint? = nil
    @Published var arrowEnd: CGPoint? = nil
    @Published var highlightPos: CGPoint? = nil
    @Published var actions: [ActionItem] = []
    @Published var statusText: String = "● ANALYZING"
    @Published var winratePercent: Int = 50
    @Published var manaText: String = "0/0"
}

struct ActionItem: Identifiable {
    let id = UUID()
    let type: String
    let desc: String
    let details: String
    
    var color: Color {
        let upperType = type.uppercased()
        if upperType.contains("PLAY") { return Color(hex: "4ec9b0") }
        if upperType.contains("ATTACK") { return Color(hex: "f14c4c") }
        if upperType.contains("HERO") { return Color(hex: "dcdcaa") }
        return Color(hex: "0078d4")
    }
}

// Main SwiftUI View
struct OverlayRootView: View {
    @ObservedObject var content: OverlayContentView
    
    var body: some View {
        ZStack {
            // Canvas for arrows and highlights
            Canvas { context, size in
                drawOverlayGraphics(context: context, size: size)
            }
            .ignoresSafeArea()
            
            // Panel UI
            VStack {
                HStack {
                    OverlayPanelView(content: content)
                        .frame(width: 340)
                    Spacer()
                }
                Spacer()
            }
            .padding(15)
        }
    }
    
    func drawOverlayGraphics(context: GraphicsContext, size: CGSize) {
        let screenWidth = size.width
        let screenHeight = size.height
        
        // Pulsing animation (simplified - use Timer for real animation)
        let pulse: CGFloat = 0.5
        
        // Draw arrow (coordinates are percentages 0.0-1.0)
        if let start = content.arrowStart, let end = content.arrowEnd {
            // Convert percentages to pixels, flip Y (macOS has flipped coordinates)
            let startPt = CGPoint(x: start.x * screenWidth, y: screenHeight - (start.y * screenHeight))
            let endPt = CGPoint(x: end.x * screenWidth, y: screenHeight - (end.y * screenHeight))
            
            // Glow
            var path = Path()
            path.move(to: startPt)
            path.addLine(to: endPt)
            context.stroke(path, with: .color(Color(hex: "f14c4c").opacity(0.3 + 0.2 * pulse)), lineWidth: 14)
            
            // Line
            context.stroke(path, with: .color(Color(hex: "f14c4c")), lineWidth: 3)
            
            // Target circle
            let radius: CGFloat = 25 + (6 * pulse)
            context.fill(
                Circle().path(in: CGRect(x: endPt.x - radius, y: endPt.y - radius, width: radius * 2, height: radius * 2)),
                with: .radialGradient(
                    Gradient(colors: [Color(hex: "f14c4c").opacity(0.6), .clear]),
                    center: endPt,
                    startRadius: 0,
                    endRadius: radius
                )
            )
            
            // Center dot
            context.fill(
                Circle().path(in: CGRect(x: endPt.x - 4, y: endPt.y - 4, width: 8, height: 8)),
                with: .color(.white.opacity(0.8))
            )
        }
        
        // Draw highlight (coordinates are percentages 0.0-1.0)
        if let pos = content.highlightPos {
            let pt = CGPoint(x: pos.x * screenWidth, y: screenHeight - (pos.y * screenHeight))
            let radius: CGFloat = 35 + (8 * pulse)
            
            // Ring
            var ringPath = Path()
            ringPath.addEllipse(in: CGRect(x: pt.x - radius, y: pt.y - radius, width: radius * 2, height: radius * 2))
            context.stroke(ringPath, with: .color(Color(hex: "4ec9b0").opacity(0.8)), lineWidth: 3)
            
            // Fill gradient
            context.fill(
                Circle().path(in: CGRect(x: pt.x - radius, y: pt.y - radius, width: radius * 2, height: radius * 2)),
                with: .radialGradient(
                    Gradient(colors: [Color(hex: "4ec9b0").opacity(0.25), .clear]),
                    center: pt,
                    startRadius: 0,
                    endRadius: radius
                )
            )
        }
    }
}

// Panel View
struct OverlayPanelView: View {
    @ObservedObject var content: OverlayContentView
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            // Header
            HStack {
                Text("DEEPMANA AI")
                    .font(.system(size: 10, weight: .bold))
                    .foregroundColor(.gray)
                    .tracking(0.5)
                Spacer()
                Text(content.statusText)
                    .font(.system(size: 9, weight: .bold))
                    .foregroundColor(Color(hex: "4ec9b0"))
            }
            
            Divider().background(Color(hex: "2a2a2a"))
            
            // Actions header
            HStack {
                Text("ACTIONS TO PERFORM")
                    .font(.system(size: 9, weight: .bold))
                    .foregroundColor(.gray)
                    .tracking(0.5)
                Spacer()
                Text("\(content.actions.count) actions")
                    .font(.system(size: 9))
                    .foregroundColor(Color(hex: "0078d4"))
            }
            
            // Action list
            if content.actions.isEmpty {
                Text("No actions available")
                    .font(.system(size: 10))
                    .foregroundColor(.gray)
                    .padding(.vertical, 10)
            } else {
                ForEach(Array(content.actions.enumerated()), id: \.element.id) { index, action in
                    ActionRowView(stepNum: index + 1, action: action)
                }
            }
            
            Divider().background(Color(hex: "2a2a2a"))
            
            // Stats row
            HStack {
                VStack(alignment: .leading, spacing: 2) {
                    Text("MANA")
                        .font(.system(size: 8, weight: .bold))
                        .foregroundColor(.gray)
                    Text(content.manaText)
                        .font(.system(size: 14, weight: .bold))
                        .foregroundColor(Color(hex: "0078d4"))
                }
                Spacer()
                VStack(alignment: .trailing, spacing: 2) {
                    Text("WIN %")
                        .font(.system(size: 8, weight: .bold))
                        .foregroundColor(.gray)
                    Text("\(content.winratePercent)%")
                        .font(.system(size: 14, weight: .bold))
                        .foregroundColor(winrateColor)
                }
            }
        }
        .padding(16)
        .background(Color(hex: "1a1a1a").opacity(0.96))
        .cornerRadius(8)
        .overlay(
            RoundedRectangle(cornerRadius: 8)
                .stroke(Color(hex: "2a2a2a"), lineWidth: 1)
        )
    }
    
    var winrateColor: Color {
        if content.winratePercent > 60 { return Color(hex: "4ec9b0") }
        if content.winratePercent < 40 { return Color(hex: "f14c4c") }
        return Color(hex: "0078d4")
    }
}

struct ActionRowView: View {
    let stepNum: Int
    let action: ActionItem
    
    var body: some View {
        HStack(spacing: 10) {
            // Step number
            Text("\(stepNum)")
                .font(.system(size: 10, weight: .bold))
                .foregroundColor(Color(hex: "1a1a1a"))
                .frame(width: 24, height: 24)
                .background(action.color)
                .cornerRadius(12)
            
            // Text
            VStack(alignment: .leading, spacing: 2) {
                Text(action.desc)
                    .font(.system(size: 11, weight: .bold))
                    .foregroundColor(action.color)
                if !action.details.isEmpty {
                    Text(action.details)
                        .font(.system(size: 9))
                        .foregroundColor(.gray)
                }
            }
            Spacer()
        }
        .padding(.horizontal, 12)
        .padding(.vertical, 10)
        .background(Color(hex: "2a2a2a"))
        .cornerRadius(6)
    }
}

// Color extension for hex
extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 6: (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default: (a, r, g, b) = (255, 0, 0, 0)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue: Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}
