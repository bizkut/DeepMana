
import sys
import torch
import platform
import os

def check_cuda():
    print("="*60)
    print(f"DeepMana CUDA Verification Tool")
    print("="*60)
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version.split()[0]}")
    print("-" * 60)

    # 1. PyTorch Check
    print("Checking PyTorch...")
    try:
        print(f"PyTorch Version: {torch.__version__}")
        if torch.cuda.is_available():
            print(f"✅  CUDA is available for PyTorch!")
            print(f"    Device Count: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"    Device {i}: {torch.cuda.get_device_name(i)}")
            
            # Test simple tensor
            x = torch.tensor([1.0]).cuda()
            print(f"    Test Tensor Location: {x.device}")
        else:
            print("❌  CUDA is NOT available for PyTorch.")
            print("    Please install the CUDA version of PyTorch.")
            print("    Command: pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121")
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
        else:
            print("⚠️  CUDA Execution Provider is MISSING.")
            print("    Ensure 'onnxruntime-gpu' is installed and valid CUDA libs are in PATH.")
            print("    Command: pip uninstall onnxruntime onnxruntime-gpu")
            print("    Command: pip install onnxruntime-gpu")
    except ImportError:
        print("⚠️  onnxruntime is not installed.")
    except Exception as e:
        print(f"❌  Error checking ONNX Runtime: {e}")

    print("="*60)

if __name__ == "__main__":
    check_cuda()
