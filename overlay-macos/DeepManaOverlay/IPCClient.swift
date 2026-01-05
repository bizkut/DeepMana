import Foundation

struct OverlayMessage {
    let type: String
    let data: [String: Any]?
}

class IPCClient {
    private let socketPath = "/tmp/deepmana_overlay.sock"
    private var inputStream: InputStream?
    private var outputStream: OutputStream?
    private var isConnected = false
    private var reconnectTimer: Timer?
    private var buffer = Data()
    
    var onMessage: ((OverlayMessage) -> Void)?
    
    func connect() {
        disconnect()
        
        // Try to connect
        var readStream: Unmanaged<CFReadStream>?
        var writeStream: Unmanaged<CFWriteStream>?
        
        CFStreamCreatePairWithSocketToHost(
            kCFAllocatorDefault,
            nil,
            0,
            &readStream,
            &writeStream
        )
        
        // Use Unix domain socket
        let socketHandle = socket(AF_UNIX, SOCK_STREAM, 0)
        guard socketHandle >= 0 else {
            scheduleReconnect()
            return
        }
        
        var addr = sockaddr_un()
        addr.sun_family = sa_family_t(AF_UNIX)
        socketPath.withCString { ptr in
            withUnsafeMutablePointer(to: &addr.sun_path.0) { dest in
                _ = strcpy(dest, ptr)
            }
        }
        
        let connectResult = withUnsafePointer(to: &addr) { ptr in
            ptr.withMemoryRebound(to: sockaddr.self, capacity: 1) { sockaddrPtr in
                Darwin.connect(socketHandle, sockaddrPtr, socklen_t(MemoryLayout<sockaddr_un>.size))
            }
        }
        
        guard connectResult == 0 else {
            close(socketHandle)
            print("[IPCClient] Connection failed, will retry...")
            scheduleReconnect()
            return
        }
        
        // Create streams from socket
        CFStreamCreatePairWithSocket(kCFAllocatorDefault, socketHandle, &readStream, &writeStream)
        
        guard let input = readStream?.takeRetainedValue(),
              let output = writeStream?.takeRetainedValue() else {
            close(socketHandle)
            scheduleReconnect()
            return
        }
        
        inputStream = input as InputStream
        outputStream = output as OutputStream
        
        inputStream?.delegate = self as? StreamDelegate
        inputStream?.schedule(in: .main, forMode: .common)
        outputStream?.schedule(in: .main, forMode: .common)
        
        inputStream?.open()
        outputStream?.open()
        
        isConnected = true
        print("[IPCClient] Connected to Python bridge")
        
        // Start reading
        startReading()
    }
    
    func disconnect() {
        reconnectTimer?.invalidate()
        reconnectTimer = nil
        
        inputStream?.close()
        outputStream?.close()
        inputStream = nil
        outputStream = nil
        isConnected = false
    }
    
    private func scheduleReconnect() {
        reconnectTimer?.invalidate()
        reconnectTimer = Timer.scheduledTimer(withTimeInterval: 2.0, repeats: false) { [weak self] _ in
            self?.connect()
        }
    }
    
    private func startReading() {
        DispatchQueue.global(qos: .utility).async { [weak self] in
            guard let self = self else { return }
            
            var buffer = [UInt8](repeating: 0, count: 4096)
            
            while self.isConnected {
                guard let stream = self.inputStream, stream.hasBytesAvailable else {
                    Thread.sleep(forTimeInterval: 0.01)
                    continue
                }
                
                let bytesRead = stream.read(&buffer, maxLength: buffer.count)
                
                if bytesRead > 0 {
                    self.buffer.append(contentsOf: buffer[0..<bytesRead])
                    self.processBuffer()
                } else if bytesRead < 0 {
                    // Error
                    DispatchQueue.main.async {
                        self.disconnect()
                        self.scheduleReconnect()
                    }
                    break
                }
            }
        }
    }
    
    private func processBuffer() {
        // Messages are newline-delimited JSON
        while let newlineIndex = buffer.firstIndex(of: UInt8(ascii: "\n")) {
            let lineData = buffer[..<newlineIndex]
            buffer = Data(buffer[(newlineIndex + 1)...])
            
            guard let jsonString = String(data: Data(lineData), encoding: .utf8),
                  let data = jsonString.data(using: .utf8),
                  let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                  let type = json["type"] as? String else {
                continue
            }
            
            let msgData = json["data"] as? [String: Any]
            let message = OverlayMessage(type: type, data: msgData)
            
            DispatchQueue.main.async { [weak self] in
                self?.onMessage?(message)
            }
        }
    }
}
