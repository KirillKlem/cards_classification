import os
import kaggle
import tensorflow as tf
import numpy as np

from tensorflow import keras


# Specify the name of the dataset and the target folder
dataset = 'gpiosenka/cards-image-datasetclassification'  #https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification
destination_folder = 'data'

# Create the target folder if not exists
os.makedirs(destination_folder, exist_ok=True)

# Download dataset
if not os.path.exists(f'{destination_folder}/train'):
    kaggle.api.dataset_download_files(dataset, path=destination_folder, unzip=True)


#Clear the data from unnecessary 
unnecessary_files = [f'{destination_folder}/14card types-14-(200 X 200)-94.61.h5',
                     f'{destination_folder}/53cards-53-(200 X 200)-100.00.h5',
                    f'{destination_folder}/cards.csv']
for f in unnecessary_files:
    if os.path.exists(f):
        os.remove(f)


train_ds = keras.preprocessing.image_dataset_from_directory(
    'data/train',
    label_mode='categorical',
    seed=123,
    image_size=(224, 224),
    batch_size=32,
    shuffle=True
)

val_ds = keras.preprocessing.image_dataset_from_directory(
    'data/valid',
    label_mode='categorical',
    seed=123,
    image_size=(224, 224),
    batch_size=32,
    shuffle=True
)

test_ds = keras.preprocessing.image_dataset_from_directory(
    'data/test',
    label_mode='categorical',
    seed=123,
    image_size=(224, 224),
    batch_size=32,
    shuffle=True
)