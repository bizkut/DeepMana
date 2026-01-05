# DeepMana macOS Native Overlay

A native Swift overlay that stays visible above Hearthstone on macOS.

## Building

### Option 1: Swift Package Manager (Recommended)

```bash
cd overlay-macos
swift build -c release
```

The built app will be at `.build/release/DeepManaOverlay`

### Option 2: Xcode

1. Open `overlay-macos` folder in Xcode
2. Build with Cmd+B
3. Or run directly with Cmd+R

## Usage

1. **Grant Accessibility Permission**: On first run, macOS will prompt you to enable accessibility for the app in System Preferences → Privacy & Security → Accessibility

2. **Start the Python assistant**: The overlay automatically connects to the Python bridge

3. **Run Hearthstone**: The overlay will float above the game window

## Architecture

```
Python (live_assistant.py)
    │
    ├─ Windows: PyQt6 OverlayWindow (direct)
    │
    └─ macOS: OverlayBridge (IPC Server)
                    │
                    └─ Unix Socket (/tmp/deepmana_overlay.sock)
                            │
                            └─ DeepManaOverlay.app (Swift)
```

## Files

- `AppDelegate.swift` - App lifecycle, accessibility check, IPC message handling
- `OverlayWindow.swift` - NSPanel with floating level, SwiftUI views
- `IPCClient.swift` - Unix socket client with auto-reconnect
- `Info.plist` - App configuration (LSUIElement for no dock icon)
