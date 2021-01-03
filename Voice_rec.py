# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:37:36 2020

@author: Adithia Jo
"""


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        if(str("home") in text):
            print ("go to home ")   ## tugas mas hari deploy easy pasti :V     
        elif(str("setting")in text):
            print ("go to setting")
        elif(str("profile")in text):
            print ("go to profile")
        elif(str("news")in text):
            print ("go to news")
        elif(str("message")in text):
            print ("go to message")
        elif(str("agenda")in text):
            print ("go to agenda")
        elif(str("gallery")in text):
            print ("go to gallery")
        elif(str("shop")in text):
            print ("go to shop")
        elif(str("order")in text):
            print ("go to order")
        elif(str("back")in text):
            print ("go to back")
        elif(str("foward")in text):
            print ("go to foward")
    
    
    except:
        print("ngomong opo ")
        

