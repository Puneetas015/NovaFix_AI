import sys
import types
import os
import warnings
import time

# --- 1. SILENCE SYSTEM CHATTER ---
warnings.filterwarnings("ignore")
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" 

# Patch for older library versions
try:
    import torchvision.transforms.functional as F
    functional_tensor = types.ModuleType('functional_tensor')
    functional_tensor.rgb_to_grayscale = F.rgb_to_grayscale
    functional_tensor.to_tensor = F.to_tensor
    sys.modules['torchvision.transforms.functional_tensor'] = functional_tensor
except ImportError:
    pass

import cv2
import numpy as np
import torch
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# --- 2. NOVAFIX ENGINE CONFIG ---
AI_READY = False
try:
    from gfpgan import GFPGANer
    from realesrgan import RealESRGANer
    from basicsr.archs.rrdbnet_arch import RRDBNet
    AI_READY = True
except Exception:
    pass

class NovaFixAI:
    def __init__(self):
        print("-" * 50)
        print("   🚀 Nova_Fix AI | Professional Studio Suite")
        print("-" * 50)
        
        # A. Neural Engine Check
        self.device = "GPU Acceleration" if torch.cuda.is_available() else "Standard CPU"
        print(f"[SYSTEM] Hardware detected: {self.device}")
        
        # B. Load AI Models
        model_path = 'selfie_segmenter.tflite'
        if not os.path.exists(model_path):
            print("[CRITICAL] Missing required AI assets. Please check root folder.")
            return
            
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.ImageSegmenterOptions(base_options=base_options, output_category_mask=True)
        self.segmenter = vision.ImageSegmenter.create_from_options(options)

        self.face_restorer = None
        if AI_READY:
            gfp_path = 'GFPGANv1.3.pth'
            if os.path.exists(gfp_path):
                model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
                upscaler = RealESRGANer(scale=4, model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth', model=model, tile=400, half=torch.cuda.is_available())
                self.face_restorer = GFPGANer(model_path=gfp_path, upscale=2, arch='clean', channel_multiplier=2, bg_upsampler=upscaler)
                print(f"[SYSTEM] AI Enhancement Engine: ONLINE")
        
        print(f"[SYSTEM] Ready for processing.\n")

    def process_image(self, filename):
        start_time = time.time()
        print(f"📦 JOB START: {filename}")
        
        img = cv2.imread(os.path.join('inputs', filename))
        if img is None:
            print(f"   └─ ❌ Error: Could not read file.")
            return

        # 1. AI Enhancement
        print(f"   ├─ Step 1/3: Restoring facial details & upscaling...")
        if self.face_restorer:
            _, _, restored = self.face_restorer.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
        else:
            restored = cv2.detailEnhance(img, sigma_s=15, sigma_r=0.15)

        # 2. Studio Masking
        print(f"   ├─ Step 2/3: Applying HD Studio segmentation...")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        seg_res = self.segmenter.segment(mp_image)
        mask = (seg_res.category_mask.numpy_view() > 0.1).astype(np.float32)
        mask = cv2.resize(mask, (restored.shape[1], restored.shape[0]))
        mask_3d = np.dstack([cv2.GaussianBlur(mask, (11, 11), 0)] * 3)

        # 3. Final Mastering
        print(f"   ├─ Step 3/3: Mastering background bokeh & color...")
        bg_blur = cv2.convertScaleAbs(cv2.GaussianBlur(restored, (41, 41), 0), alpha=0.85, beta=-10)
        final = (mask_3d * restored.astype(float)) + ((1 - mask_3d) * bg_blur.astype(float))
        
        save_path = os.path.join('outputs', f'NovaFix_{filename}')
        cv2.imwrite(save_path, final.clip(0, 255).astype(np.uint8))
        
        elapsed = time.time() - start_time
        print(f"   └─ ✅ SUCCESS: Rendered in {elapsed:.1f}s\n")

if __name__ == "__main__":
    os.makedirs('inputs', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)
    app = NovaFixAI()
    files = [f for f in os.listdir('inputs') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if not files:
        print("ℹ️ No images found in 'inputs' folder. Please add some!")
    for f in files:
        app.process_image(f)