from flask import Flask, render_template, Response, request, jsonify
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.7)


app = Flask(__name__)


def talk(text):
    engine.say(text)


@app.route('/', methods=['GET', 'POST'])
def take_command():
    return render_template('index.html')


@app.route('/playme', methods=['GET', 'POST'])
def playme():

    return render_template('index.html')


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        myval = request.form["speechToText"]
        if "play" in myval:
            print("My Value ", myval)
            pywhatkit.playonyt(myval)
            return myval
        elif "stop" in myval:
            talk('stoping...... ')
            os.system("taskkill /im chrome.exe /f")
        else:
            talk('speak again')

    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True)
