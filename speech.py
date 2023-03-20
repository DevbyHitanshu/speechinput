#from flask import Flask, render_template, Response
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import nltk


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.7)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ninja' in command:
                command = command.replace('ninja', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing...... ' + song)
        pywhatkit.playonyt(song)
    elif 'stop ' in command:
        song = command.replace('play', '')
        talk('stoping...... ' + song)
        os.system("taskkill /im chrome.exe /f")
    else:
        print("speak again")
        talk("speak again")


while True:
    run_alexa()
