# PanoDiff-SR: Synthesizing Dental Panoramic Radiographs using Diffusion and Super-resolution

[![Paper](https://img.shields.io/badge/ECAI-2025-red)]()
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange)](https://pytorch.org/)
[![pyngrok](https://img.shields.io/badge/PyNgRok-7.2%2B-yellow)](https://pytorch.org/)


<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/wvClGg717OZvK86TCILc0EUC5ckEHvGn/image.png" alt="PanoDiff Teaser" width="800"/>
</p>

> 📢 Official PyTorch implementation of the **ECAI 2025** accepted paper:  
> **PanoDiff-SR: Synthesizing Dental Panoramic Radiographs using Diffusion and Super-resolution**  
> Sanyam	Jain, Bruna	Neves de Freitas, Andreas	Basse-O'Connor, Alexandros	Iosifidis, Ruben	Pauwels
> [[Demo]](https://github.com/s4nyam/PanoDiff) | [[Code]](https://github.com/s4nyam/PanoDiff)

---

## 🔥 News
- **May 2025:** PanoDiff submitted to **ECAI 2025**! 🎉
- This repository supersedes previous work, **PanoGAN** [[PanoGAN Paper]](https://www.mdpi.com/2313-433X/11/2/41), with advanced methods and updated code.

---

## 🌟 Highlights
- **Modular Design:** Two learning algorithms are used **Diffusion (DDPM, DDIM)** and **Super-Resolution (ST-transformer)** trained independently.
- **Dataset:** Uses **five public datasets** with varying preprocessing and postprocessing inlcuding resize, rotation and crop.
- **Diffusion:** Uses simple denoisinng diffusion probabilistic model for syntehsis with a attention-aware UNet backbone.
- **SR:** Built upon **HAT-SR** with novel losses - pixel-wise loss (L_1), perceptual loss (L_percep), and adversarial loss (L_GAN).
- **Real-vs-Fake Quiz:** A time-limited human in the loop activity to identify a given image as real or synthetic? Six dentists with varying experience were invited to play the quiz for 200 images (100 real and 100 fake).

<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/zu86EKZKoUyEMb84i8AmwbSd9nsM5knc/image.png" alt="Selected Examples" width="800"/>
  <br>
  <em>Selected **synthetic examples** from our work that fooled most dentists.</em>
</p>


## 📊 Dataset

<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/fNlF9Ytp2g0cGoIaGoekrZmB550SMKZh/image.png" alt="T sne" width="500"/>
</p>

T-distributed stochastic neighbor embedding (t-SNE) plot of 500 random images picked from each source dataset.

**Table**: Overview of dental radiography datasets used in our study. * indicates that the dataset was recently updated with 1500 more images, but we accessed it when it had 500 images. ~ indicates varying sizes in the dataset within the given resolution range. Abbreviations: ADLD – A dual-labeled dataset, DENTEX – Dental Enumeration and Diagnosis on Panoramic X-rays, TSXK – Teeth Segmentation on dental X-ray images, TUFTS – Tufts Dental Database, USPFORP – São Paulo dataset.

| Abbr.    | Images | Format | Availability | Year | Country | Resolution |
|---|---|---|---|---|---|---|
| [ADLD](https://www.kaggle.com/datasets/zwbzwb12341234/a-dual-labeled-dataset) | 500* | png | Kaggle | 2024 | China | ~2940×1435 or ~987×478 |
| [DENTEX](https://zenodo.org/records/7812323#.ZDQE1uxBwUG) | 3903 | png | Zenodo | 2023 | Switzerland | ~2950×1316 or ~1976×976 |
| [TSXK](https://www.kaggle.com/datasets/humansintheloop/teeth-segmentation-on-dental-x-ray-images) | 1196 | png | Kaggle | 2023 | DR Congo | 2041×1024 |
| [TUFTS](https://tdd.ece.tufts.edu/) | 1000 | jpg | On Request | 2022 | USA | 1615×840 |
| [USPFORP](https://pubmed.ncbi.nlm.nih.gov/38632036/) | 936 | jpg | On Request | 2024 | Brazil | 2903×1536 |

---

## 🧠 Overview

<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/CcSvKjSuqpj8wKQwb9XBlE4l9Br129wS/image.png" alt="PanoDiff Architecture" width="800"/>
  <br>
  <em>Figure: General principle of synthetic image generation through manifold representation. Consider a dataset of images {x<sub>k</sub>}<sub>k=1</sub><sup>n</sup>, where x<sub>k</sub> ∼ p(x). These images serve as samples from the target distribution p(x). A best sampler G<sub>θ</sub> is one such that x̂ = G<sub>θ</sub>(z), where z ∼ 𝒩(0, I), to produce high-quality samples resembling the true data distribution p.</em>
</p>

For the top-most figure in this readme:
<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/wvClGg717OZvK86TCILc0EUC5ckEHvGn/image.png" alt="PanoDiff Working Process" width="800"/>
  <br>
  <em>Figure: Working of PanoDiff in three key steps: (1) In the forward phase, noise is added to the input image x<sub>t=0</sub> over t=1000 time steps, following a β-schedule (slow-start and fast-finish). The plot on the right shows pixel variation metrics converging to 0.5 because the image is pure noise at t=1000. (2) The reverse phase (in left) involves training a U-Net (using L<sub>1</sub> loss), shown on the left, such that it takes a random source image with a random noisy image at t. The trained U-Net predicts most of the noise given a noisy image at t. For comparison, an old method is shown (in right), which performs denoising through a slow, stochastic, step-by-step process, requiring hundreds to thousands of iterations to gradually remove noise using the frozen U-Net from the previous step (on the left). (3) The image generation process in PanoDiff involves iteratively predicting and removing noise from a noisy image x<sub>t=0</sub> using a frozen U-Net, resulting in a slightly less noisy image. The resulting image is added with noise and fed to the U-Net, which again predicts and removes noise. This process continues for <em>inference</em> time steps.</em>
</p>

---

## 📄 Visiblity (Need to update later)
**PanoDiff-SR: Synthesizing Dental Panoramic Radiographs using Diffusion and Super-resolution**  
Sanyam Jain, Bruna Neves de Freitas, Andreas Basse-O'Connor, Alexandros	Iosifidis, Ruben Pauwels
*European Conference on Artificial Intelligence (ECAI) 2025*  
[[GitHub]](https://github.com/s4nyam/panodiff) | [[PDF]](https://github.com/s4nyam/panodiff) | [[Project]](https://github.com/s4nyam/panodiff) | [[Results]](https://github.com/s4nyam/panodiff) | [[TarBall]](https://github.com/s4nyam/panodiff) 

---

## 📑 Table of Contents
- [Installation](#installation)
- [Model Zoo](#model-zoo)
- [Data Preparation](#data-preparation)
- [Training](#training)
- [Evaluation](#evaluation)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shahzadnit/T2L.git
   cd T2L
   ```

2. **Create a virtual environment:**
   ```bash
   conda create -n t2l python=3.8
   conda activate t2l
   pip install -r requirements.txt
   ```

3. **Install PyTorch:**
   Install PyTorch following instructions from [PyTorch's official site](https://pytorch.org/).

---

## 🧪 Model Zoo

All models utilize the **CLIP ViT-B/16** backbone and are trained on **Kinetics-400** unless otherwise specified.

### 🔍 Zero-Shot Evaluation
Models are trained on Kinetics-400 and evaluated directly on downstream datasets.

| **Model**      | **Input** | **HMDB-51** | **UCF-101** | **Kinetics-600** | **Model Download** |
|----------------|:---------:|:-----------:|:-----------:|:----------------:|:-------------------:|
| **T2L (ViT-16)** | 8×224     | **52.9**     | **79.1**     | **70.1**           | [📥 Link](https://drive.google.com/file/d/19QNGgaZjPyq0yz7XJGFccS7MV09KMY_K/view?usp=drive_link) |

### 🔀 Base-to-Novel Generalization
Models are trained on base classes and evaluated on both base and novel classes.

| **Dataset** | **Input** | **Base Acc.** | **Novel Acc.** | **Harmonic Mean (HM)** | **Model Download** |
|-------------|:---------:|:-------------:|:---------------:|:-----------------------:|:-------------------:|
| **Kinetics-400** | 8×224 | 73.1 | 60.6 | **66.3** | [📥 Link](https://drive.google.com/file/d/1q8rBkL0QKNTeJJihWkNUwm1eAGH_OY0U/view?usp=sharing) |
| **HMDB-51**      | 8×224 | 77.0 | 58.2 | **66.3** | [📥 Link](https://drive.google.com/file/d/1hW2i6agAhpyFvoRgPcOki3coQHx-6oWN/view?usp=sharing) |
| **UCF-101**      | 8×224 | 94.4 | 77.9 | **85.4** | [📥 Link](https://drive.google.com/file/d/16HTxwbqfi1N8BPVjfrvL6F_A4xLNt-zc/view?usp=sharing) |
| **SSv2**         | 8×224 | 16.6 | 13.3 | **14.8** | [📥 Link](https://drive.google.com/file/d/1EtpET-s634JnHK7n57vrvqNpE7qH_dHq/view?usp=sharing) |

---

## 🗂️ Data Preparation

Pre-extract video frames for efficient training and evaluation using scripts in `Dataset_creation_scripts`.

**Supported Datasets:**
- 🎞️ [Kinetics-400/600](https://deepmind.com/research/open-source/open-source-datasets/kinetics/)
- 📺 [UCF-101](http://crcv.ucf.edu/data/UCF101.php)
- 🎬 [HMDB-51](http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/)
- 🎬 [Something-Something-v2](https://developer.qualcomm.com/software/something-something-video-dataset)

**Steps:**
1. Download datasets from their official websites.
2. Extract frames:
   ```bash
   python Dataset_creation_scripts/extract_frames.py --dataset <dataset_name> --data_path <path_to_videos>
   ```
3. Update dataset paths in configuration files (`configs/<dataset>/*.yaml`).

---

## 🏋️ Training

Train T2L with the provided configuration files:
```bash
python train.py --config configs/K-400/k400_train.yaml
```

**Training Details:**
- **Backbone:** CLIP ViT-B/16
- **Optimizer:** AdamW, learning rate 5e-5
- **Epochs:** 50
- **Batch Size:** 70
- **Hardware:** Single NVIDIA A100 80GB GPU

---

## 🧪 Evaluation

Evaluate pre-trained models:
```bash
python test.py --config configs/ucf101/UCF_zero_shot_testing.yaml
```

**Evaluation Settings:**
- **Zero-Shot:** HMDB-51, UCF-101, Kinetics-600
- **Base-to-Novel:** Base and novel classes
- **Few-Shot:** K={2,4,8,16} shots

---

## 📖 Citation

If you find this work useful, please cite our paper:

```bibtex
@article{
ahmad2025tl,
title={T2L: Efficient Zero-Shot Action Recognition with Temporal Token Learning},
author={Shahzad Ahmad and Sukalpa Chanda and Yogesh S Rawat},
journal={Transactions on Machine Learning Research},
issn={2835-8856},
year={2025},
url={https://openreview.net/forum?id=WvgoxpGpuU},
note={}
}
```

---

## 🙏 Acknowledgments

- Built upon [ActionCLIP](https://github.com/sallymmx/ActionCLIP).
- Gratitude to the open-source community for datasets and tools.
- Supported by Østfold University College and the University of Central Florida.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
