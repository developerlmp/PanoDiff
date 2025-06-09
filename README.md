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
> [[Project]](https://github.com/s4nyam/PanoDiff) | [[Code]](https://github.com/s4nyam/PanoDiff)

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
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Installation

1. **Installation:**
   ```bash
   git clone https://github.com/s4nyam/PanoDiff.git
   cd panodiff
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Install PyTorch:**
   Install PyTorch following instructions from [PyTorch official site](https://pytorch.org/).

**requirements.txt**
```markdown
h5py
matplotlib
natsort
numpy
opencv_contrib_python
pandas
scipy
tqdm
retinaface-pytorch
diffusers
basicSR
einops
nvitop
flask
firebase-admin
pyngrok
```

---

## Model Zoo
Pretrained Models for PanoDiff and SR are avaialble here in table below: 

(Coming Soon!)

---

## Training

Train PanoDiff and SR with the provided "how-to" files in each nested directories.


**Training Details:**

| Configuration      | Lowest            | Highest          |
|--------------------|-------------------|------------------|
| GPU               | RTX 6000 48GB × 1 | A100 80GB × 4    |
| RAM               | 128 GB            | 256 GB           |
| Train Batch       | 4                 | 16               |
| Evaluation Batch  | 16                | 48               |
| Input Resolution  | 256×128×3         | 256×128×3        |

---

## Evaluation

(Coming Soon!)

---

## Results

<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/Z4p3O7Esis2b0kpeELr1jCW0cqzf9kRD/image.png" alt="PanoDiffSR Epochs" width="800"/>
  <br>
  <em>Figure: Comparison of generated PRs across epochs. Each column represents a different epoch from left to right, showing the images generated using same unique seed per row.</em>
</p>


<p align="center">
  <img src="https://dl3.pushbulletusercontent.com/IWhTJVlMsVK41NLhMmhx5sQREorwb4j6/image.png" alt="Results from Dentists" width="800"/>
  <br>
  <em>Table: Real vs synthetic image combinations and respective Fréchet inception distance (FID). Lower scores indicate greater similarity. <br/> Figure: Pie charts for each observer showing distribution of correct and incorrect decisions. ‘Fully’ and ‘partially’ refers to the level of certainty indicated by the observer for a given answer, as described in the text.</em>
</p>

---

## Citation

(Coming Soon!)

If you find this work useful, please cite our paper:

```bibtex

```

---

## Acknowledgments

- Gratitude to the open-source community for datasets and tools.
- Together with Dept of Dentistry and Oral Health AU Denmark, Dept of Mathematics AU Denmark, and Computer Science Unit Tampere University Finland.
- Computing resources were supported by ECE and MaLeCi Aarhus University, Denmark

---

## License

(Coming Soon!)
