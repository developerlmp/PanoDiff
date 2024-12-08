# Diffusion Model
The simple diffusion model is used to generate low-resolution panoramic synthetic radiograph images of size 128X256. The model takes input of 512X1024 image size and gets trained. There are total of 7243 xray images taken from different datasets to train the diffusion model. The directory structure is as follows:

## Folders

- **generated_samples**: Seed wise folders of generated images. These images are generated using a pretrained model and python file `generate.py`. You can change `seedvalue` to decide how many samples are gomna be created, for example for seed value 500 it produces 500 (each seed) * 32 (batch of different) images. In the same python file you can change `eval_batch_size` to decide how many samples you want to draw from the trained model. Argument `pretrained_model_path` with drafuly value as `default=trained_models/ddpm-model-ep574.pth` uses a pretrained model to generated images.

- **images**: There are total of 7243 images downloaded from different datasets. You can request this dataset as zip file at `sanyam.jain@dent.au.dk`

- **simple_diffusion**: Folder with diffusion model classes.

- **test_samples**: Generated output images of size 128X256.

- **trained_models**: Trained models are saved in this folder.

## Files

- **create_generated_data.py**: This file converts jepg to png while skipping grid.jpeg files from each of the `geneated_samples` folder

- **generate.py**: This file generates sample images from pretrained model.

- **train.py**: This file trains the simple diffusion model.

## Run How to 

`python train.py`

`python generate.py`

