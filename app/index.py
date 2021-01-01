from flask import Flask, request, url_for, render_template
import speech_recognition as sr

app = Flask(__name__)
r = sr.Recognizer() 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['mp3file']
        with sr.AudioFile(f) as source:
            audio = r.record(source) 
        text = r.recognize_google(audio,language="my-MM")
    return render_template("result.html",audio=text )

if __name__== '_main_':
    app.run()