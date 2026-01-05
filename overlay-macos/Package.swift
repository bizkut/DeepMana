// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "DeepManaOverlay",
    platforms: [
        .macOS(.v12)
    ],
    targets: [
        .executableTarget(
            name: "DeepManaOverlay",
            path: "DeepManaOverlay"
        )
    ]
)
