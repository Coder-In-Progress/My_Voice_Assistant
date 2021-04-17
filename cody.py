from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

text = get_audio()

if "hello" in text:
  speak ("Hello")

if "Who is the greatest person in the universe" in text:
  speak ("Jithesh is the best")

if "What is your name" in text:
  speak ("My name is Zen")

if "Tell me a fact about yourself" in text:
  speak ("I am not so virtual. In fact, I am everywhere, in your dreams, and I haunt you... Muheheheheheheaaaaaa")



WAKE_WORD = "Zen"
