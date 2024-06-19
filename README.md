## Introduction
Hello! It's my pet-project for upgrading and demonstrating my skills.

The motivation to do this project comes from the fact that I wanted to try to create my own neural network, so a dataset from Kaggle was taken (https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification ), on the basis of which the project was created. The essence of the project is to classify (determine what kind of card it is) playing cards by photo.

Name|Description| Stack
-----------|:-------:|:--------: 
Cards classification| Upload data, create a basic cas, create a CNN using fine-tuning, visualize the learning process by epoch | Tensorflow, keras, scikit-learn

## Disclaimer
So far, this model is not optimal and is under development. There are many more ways to improve the metrics of the model, which will be tried in the near future.

## Main part of project
### First draft of the project
Initially, there was a desire to train your neural network from scratch. The initial idea used methods such as data augmentation, residual blocks, and batch normalization. The architecture was somewhat similar to Xception, but with a strong correction for the specifics of the task. However, not having the necessary capabilities (capacities and time), I was forced to abandon this idea and create a model using fine-tuning.

### Uploading data
The kaggle dataset was used as a basis (https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification ) (moreover, the weights of the model that are attached to the dataset were not used and were deleted at the data loading stage). A file has been created for this purpose load_data.py it creates a data folder by uploading data there. Three datasets were also created: train, validation and test, which were imported into the main file. <br>
P.S. All dependencies are in requirements.txt

### Creating base case and model
To understand how effective the use of the deep learning model is, a base case must be created that needs to be surpassed. This was the random classifier with sklearn metrics. <br>
The ConvNext model (Tiny version due to limited resources) was used as the basis for the neural network itself. AdamW was chosen as an optimizer with a low learning rate (since we use fine-tuning). The loss function uses "categorical_crossentropy" because the labels themselves are encoded using label_mode='categorical'.

### Other details
All training takes place in google colab using the gpu. Various architectures were tried at an early stage, as well as other bases for the model (for example, Swin, Vit, EfficientNet). Loss and accuracy are visualized for tracking on train and validation data. It is planned to use TensorBoard for this
