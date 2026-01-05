import Cocoa
import SwiftUI

// Explicit main entry point
let app = NSApplication.shared
let delegate = AppDelegate()
app.delegate = delegate
app.run()

class AppDelegate: NSObject, NSApplicationDelegate {
    var overlayWindow: OverlayWindow?
    var ipcClient: IPCClient?
    
    func applicationDidFinishLaunching(_ notification: Notification) {
        checkAccessibilityPermissions()
        
        overlayWindow = OverlayWindow()
        
        ipcClient = IPCClient()
        ipcClient?.onMessage = { [weak self] message in
            self?.handleMessage(message)
        }
        ipcClient?.connect()
        
        print("[DeepManaOverlay] Started")
    }
    
    func applicationWillTerminate(_ notification: Notification) {
        ipcClient?.disconnect()
    }
    
    func checkAccessibilityPermissions() {
        let options: NSDictionary = [kAXTrustedCheckOptionPrompt.takeUnretainedValue() as String: true]
        let accessEnabled = AXIsProcessTrustedWithOptions(options)
        if !accessEnabled {
            print("[DeepManaOverlay] Accessibility permission required.")
        }
    }
    
    func handleMessage(_ message: OverlayMessage) {
        DispatchQueue.main.async { [weak self] in
            guard let overlay = self?.overlayWindow?.overlayView else { return }
            
            switch message.type {
            case "arrow":
                if let data = message.data,
                   let startDict = data["start"] as? [String: Any],
                   let endDict = data["end"] as? [String: Any],
                   let sx = startDict["x"] as? Double,
                   let sy = startDict["y"] as? Double,
                   let ex = endDict["x"] as? Double,
                   let ey = endDict["y"] as? Double {
                    overlay.arrowStart = CGPoint(x: sx, y: sy)
                    overlay.arrowEnd = CGPoint(x: ex, y: ey)
                    overlay.highlightPos = nil
                } else {
                    overlay.arrowStart = nil
                    overlay.arrowEnd = nil
                }
            case "highlight":
                if let data = message.data,
                   let x = data["x"] as? Double,
                   let y = data["y"] as? Double {
                    overlay.highlightPos = CGPoint(x: x, y: y)
                    overlay.arrowStart = nil
                    overlay.arrowEnd = nil
                } else {
                    overlay.highlightPos = nil
                }
            case "actions":
                if let data = message.data,
                   let items = data["items"] as? [[String: Any]] {
                    overlay.actions = items.compactMap { item in
                        guard let type = item["type"] as? String,
                              let desc = item["desc"] as? String else { return nil }
                        let details = item["details"] as? String ?? ""
                        return ActionItem(type: type, desc: desc, details: details)
                    }
                }
            case "status":
                if let data = message.data, let text = data["text"] as? String {
                    overlay.statusText = text
                }
            case "winrate":
                if let data = message.data, let percent = data["percent"] as? Int {
                    overlay.winratePercent = percent
                }
            case "mana":
                if let data = message.data, let current = data["current"] as? Int, let max = data["max"] as? Int {
                    overlay.manaText = "\(current)/\(max)"
                }
            case "quit":
                NSApplication.shared.terminate(nil)
            default:
                break
            }
        }
    }
}
