# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:17:20 2019

@author: pk
"""

from rasa.nlu.train import train
import os


os.chdir('data')
DATA_PATH = os.path.abspath("nlu.md")
CONFIG_PATH = os.path.abspath("config.yml")
MODELS_PATH = os.path.abspath('models')
MODEL_NAME = 'classify_audio'
#c = RasaNLUModelConfig({'language' : 'en', 'pipeline' : 'supervised_embeddings'})

train(CONFIG_PATH,DATA_PATH, MODELS_PATH, MODEL_NAME)

MODELS_PATH = os.path.abspath("models")