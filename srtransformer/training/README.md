# Training Module

The training module contians all the model classes and the commands to start training. It uses regular Basic SR wrapper and commands to use `options/train` and `options/test`config files to configure the datasets folders (LQ and HR) along with hyperparameters.

python train.py -opt options/train/train_HAT_SRx2_from_scratch.yml

python test.py -opt options/test/HAT_SRx2.yml
------------------------------------------------------
python train.py -opt options/train/train_Real_HAT_GAN_SRx4_finetune_from_mse_model.yml

python test.py -opt options/test/HAT_GAN_Real_SRx4.yml
------------------------------------------------------
