from comet_ml import ConfusionMatrix, Experiment

import os
import multiprocessing
import time
from collections import Counter, OrderedDict
from pathlib import Path

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.callbacks import Callback, EarlyStopping
from keras.layers import BatchNormalization
from keras.layers.convolutional import MaxPooling2D, Conv2D
from keras.layers.core import Dense, Dropout, Flatten
from keras.models import load_model, Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from loguru import logger
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import constants

import config

# To use Comet ML visualization and logging you have to follow the instructions from README.md
# on how to set COMET_API_KEY, COMET_WORKSPACE, COMET_PROJECT_NAME environment variables
# Alternatively, you can set these variables manually in the code here by uncommenting the lines below
# os.environ["COMET_API_KEY"] = 'YOUR_API_KEY'
# os.environ["COMET_WORKSPACE"] = 'YOUR_WORKSPACE'
# os.environ["COMET_PROJECT_NAME"] = 'YOUR_PROJECT_NAME'

USE_COMET_ML = config.COMET_API_KEY and config.COMET_WORKSPACE \
            and config.COMET_PROJECT_NAME

if USE_COMET_ML:
   print("clear")
else:
    print("false")
