"""
Created on Sat Sep  7 22:34:20 2019

@author: pk
"""

from pydub import AudioSegment 
import speech_recognition as sr 
import os

def segment_audio(audioname):
    audio = AudioSegment.from_wav(audioname) 
    n = len(audio) 
    
    counter = 1
    interval = 10 * 1000
    overlap = 1 * 1000
    start = 0
    end = 0
    flag = 0
    os.chdir('..')
    os.chdir('chunks')
    for i in range(0, 2 * n, interval): 
    	if i == 0: 
    		start = 0
    		end = interval 
    	else: 
    		start = end - overlap 
    		end = start + interval 
    	if end >= n: 
    		end = n 
    		flag = 1
    	chunk = audio[start:end] 
    	filename = 'chunk'+str(counter)+'.wav'
    	chunk.export(filename, format ="wav") 
    	print("Processing chunk "+str(counter)+". Start = "+str(start)+" end = "+str(end)) 
    	counter = counter + 1
    