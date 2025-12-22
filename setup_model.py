import os
import requests

def download_ai_asset(url, filename):
    """
    Handles the downloading of neural network weights with status updates.
    """
    if os.path.exists(filename):
        print(f"[-] {filename} already exists. Skipping download.")
        return

    print(f"[!] Starting download: {filename}... Please wait.")
    try:
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        file_size = os.path.getsize(filename)
        print(f"✅ Success! {filename} ({file_size} bytes) is now ready.")
    except Exception as e:
        print(f"❌ Critical Error downloading {filename}: {e}")

if __name__ == "__main__":
    print("="*60)
    print("   🚀 NOVAFIX AI | Neural Asset Downloader")
    print("="*60)

    # Dictionary of required models: { Filename: Download_URL }
    assets = {
        "selfie_segmenter.tflite": "https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite",
        "GFPGANv1.3.pth": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth"
    }

    for filename, url in assets.items():
        download_ai_asset(url, filename)

    print("\n[+] All engines are primed. You can now run 'python main.py'.")
