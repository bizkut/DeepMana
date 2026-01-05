
import sys
import torch
import platform
import os

def check_gpu():
    print("="*60)
    print(f"DeepMana GPU Verification Tool")
    print("="*60)
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version.split()[0]}")
    print("-" * 60)

    # 1. PyTorch Check
    print("Checking PyTorch...")
    try:
        print(f"PyTorch Version: {torch.__version__}")
        
        # Check CUDA
        if torch.cuda.is_available():
            print(f"✅  CUDA is available!")
            print(f"    Device Count: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"    Device {i}: {torch.cuda.get_device_name(i)}")
            
            # Test simple tensor
            x = torch.tensor([1.0]).cuda()
            print(f"    Test Tensor Location: {x.device}")
        else:
            print("ℹ️  CUDA is NOT available.")
            
        # Check MPS (Apple Silicon)
        if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            print(f"✅  MPS (Apple Silicon GPU) is available!")
            # Test simple tensor
            x = torch.tensor([1.0]).to("mps")
            print(f"    Test Tensor Location: {x.device}")
        elif platform.system() == "Darwin":
            print("ℹ️  MPS is NOT available (requires Apple Silicon + macOS 12.3+).")
        
        # Summary
        print("-" * 60)
        if torch.cuda.is_available():
            print("🎯 Recommended device: CUDA")
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            print("🎯 Recommended device: MPS (Apple Silicon)")
        else:
            print("🎯 Using CPU (no GPU acceleration available)")
            
    except Exception as e:
        print(f"❌  Error checking PyTorch: {e}")

    print("-" * 60)

    # 2. ONNX Runtime Check
    print("Checking ONNX Runtime...")
    try:
        import onnxruntime as ort
        print(f"ONNX Runtime Version: {ort.__version__}")
        providers = ort.get_available_providers()
        print(f"Available Providers: {providers}")
        
        if 'CUDAExecutionProvider' in providers:
            print("✅  CUDA Execution Provider is available!")
        elif 'CoreMLExecutionProvider' in providers:
            print("✅  CoreML Execution Provider is available! (Apple)")
        else:
            print("ℹ️  GPU Execution Provider is not available.")
            print("    Using: CPUExecutionProvider")
    except ImportError:
        print("⚠️  onnxruntime is not installed.")
    except Exception as e:
        print(f"❌  Error checking ONNX Runtime: {e}")

    print("="*60)

if __name__ == "__main__":
    check_gpu()
