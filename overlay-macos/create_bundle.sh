#!/bin/bash
set -e

APP_NAME="DeepManaOverlay.app"
BINARY_SOURCE=".build/release/DeepManaOverlay"
PLIST_SOURCE="DeepManaOverlay/Info.plist"

echo "Creating $APP_NAME..."

if [ ! -f "$BINARY_SOURCE" ]; then
    echo "Error: Binary not found at $BINARY_SOURCE. Run 'swift build -c release' first."
    exit 1
fi

mkdir -p "$APP_NAME/Contents/MacOS"
mkdir -p "$APP_NAME/Contents/Resources"

cp "$BINARY_SOURCE" "$APP_NAME/Contents/MacOS/DeepManaOverlay"
cp "$PLIST_SOURCE" "$APP_NAME/Contents/Info.plist"

# Remove quarantine attribute to prevent "App is damaged" errors
xattr -cr "$APP_NAME"

echo "Success! $APP_NAME created."
echo "You can now drag this to /Applications if you wish."
