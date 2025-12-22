import requests
import os

# Updated URL from the official MediaPipe storage
url = "https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite"

print("Starting download of the new model... please wait.")

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status() 
    
    # We will save it as the same name our main.py expects
    with open("selfie_segmenter.tflite", "wb") as f:
        f.write(response.content)
    
    file_size = os.path.getsize("selfie_segmenter.tflite")
    print(f"✅ Success! Downloaded {file_size} bytes.")
    print("The model 'selfie_segmenter.tflite' is now ready.")

except Exception as e:
    print(f"❌ Failed to download: {e}")