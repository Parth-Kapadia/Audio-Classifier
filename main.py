"""
Created on Sat Sep  7 22:34:20 2019
@author: pk
"""


import speech_recognition as sr 
from speech2text import segment_audio
from rasa.nlu.train import train
import os
from rasa.nlu.model import Interpreter
import csv
import requests, zipfile, io

def start(zip_file_url):
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    os.chdir('audios')
    z.extractall()
    os.chdir('..')
    
    directory = os.path.abspath('audios')
    for filename in os.listdir(directory):
        audioname=filename
        os.chdir('audios')
        segment_audio(audioname)  
        
        AUDIO_FILE = ("chunk2.wav") 
          
        # use the audio file as the audio source 
          
        r = sr.Recognizer() 
          
        with sr.AudioFile(AUDIO_FILE) as source: 
            #reads the audio file. Here we use record instead of 
            #listen 
            audio = r.record(source)   
            
            intent =  r.recognize_google(audio)
          
        try: 
            print("The audio file contains: " + intent) 
          
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio") 
          
        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
          
        os.chdir('..')
        MODELS_PATH = os.path.abspath('models')
        nlu_model = Interpreter.load(os.path.join(MODELS_PATH,'classify_audio'))
        
        result = nlu_model.parse(intent)
        with open('MatrixSquadron_I-LCVDL.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([audioname,result['intent']['name']])
            

        
if __name__ == "__main__":
    start("https://ai-hackathon-upload.s3.ap-south-1.amazonaws.com/public/data.zip")