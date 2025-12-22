# NovaFix AI



<div align="center">

[![PyPI](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![LICENSE](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Open issue](https://img.shields.io/github/issues/Puneetas015/NovaFix_AI)](https://github.com/Puneetas015/NovaFix_AI/issues)

</div>

<br>

1. :boom: **Practical Application**: This project implements a studio-quality production pipeline for blind face restoration and portrait enhancement.
1. :rocket: **Optimized for Windows**: This version is a *clean* build of NovaFix AI, which runs without complex CUDA extensions, making it fully compatible with **Windows** and **Standard CPU/GPU modes**.
1. **Background Enhancement**: Integrated with **Real-ESRGAN** to ensure that non-face regions (backgrounds) are as sharp as the restored faces.

> :star: **NovaFix AI** aims at developing a **Practical Algorithm for Real-world Face Restoration**. It leverages rich priors from pretrained GANs to transform low-quality, blurry, or noisy photos into high-definition professional portraits.

<br>

---

## 🖼️ Visual Results (NovaFix Studio Render)

Below are the results generated using the NovaFix AI production pipeline, showcasing face restoration combined with cinematic bokeh effects.

| Original Sample | NovaFix AI Enhanced Output |
| :---: | :---: |
| <img src="input_sample/Julia_Roberts_crop.png" width="350"> | <img src="assets/NovaFix_Julia_Roberts_crop.png" width="350"> |
| <img src="input_sample/Adele_crop.png" width="350"> | <img src="assets/NovaFix_Studio_Adele_crop.png" width="350"> |
| <img src="input_sample/Blake_Lively.jpg" width="350"> | <img src="assets/NovaFix_Studio_Blake_Lively.jpg" width="350"> |

> **Note:** These samples demonstrate the high-fidelity identity preservation and background neural-blurring (Bokeh) capabilities of the v1.3 build.

---

:triangular_flag_on_post: **Updates**

- :white_check_mark: **Production Build**: Integrated `main.py` for automated batch processing of images.
- :white_check_mark: **V1.3 Support**: Optimized for the **[GFPGAN V1.3 model](https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth)**, which produces more natural textures and maintains identity better than previous versions.
- :white_check_mark: **Studio Bokeh**: Added a custom neural segmentation layer via MediaPipe to create professional depth-of-field effects.

---

### :book: NovaFix AI: Production-Ready Blind Face Restoration

NovaFix AI combines several state-of-the-art models into a single executable pipeline:
* **Face Restoration**: GFPGAN (Generative Facial Prior)
* **Background Upscaling**: Real-ESRGAN
* **Portrait Segmentation**: MediaPipe Selfie Segmenter

---

## :wrench: Dependencies and Installation

- Python >= 3.7
- [PyTorch >= 1.7](https://pytorch.org/)
- NVIDIA GPU + CUDA (Optional for acceleration)

### Installation

1. **Clone the repository**
    ```bash
    git clone [https://github.com/Puneetas015/NovaFix_AI.git](https://github.com/Puneetas015/NovaFix_AI.git)
    cd NovaFix_AI
    ```

1. **Install dependent packages**
    ```bash
    pip install -r requirements.txt
    ```

---

## :zap: Quick Inference

**1. Download Pre-trained Models**
To run the project, place the following models in the root directory:
* [GFPGANv1.3.pth](https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth)
* [selfie_segmenter.tflite](https://developers.google.com/mediapipe/solutions/vision/selfie_segmenter#models)

**2. Process Images**
Place your images in the `inputs/` folder and run:
```bash
python main.py
