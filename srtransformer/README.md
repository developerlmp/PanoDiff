# Super Resolution Transformer
SR transformer upscales the low resolution images to high resolution images to 2X, 3X or 4X. We train SR Transformer to perform 4X upscaling. The methodology to use SR Transformer is as follows.

## Training
Once the `images` folder is ready with the dataset, we use python scripts to low scale the original 512X1024 images to 256X512 (2X) and 128X256 (4X) low resolution of the images that are

- 512X1024 is HR (High Resolution)

- 256X512 is LQ2 (Low Resolution 2X)

- 128X256 is LQ4 (Low Resolution 4X)


## Testing and Evaluation

We test the trained model on diffuion generated images that are 128X256 to upscale it 4X. Please reach us at sanyam.jain@dent.au.dk to request the trained models.
