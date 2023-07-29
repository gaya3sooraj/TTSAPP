from flask import Flask, render_template, request
from flask_gtts import gtts
import os

app = Flask(__name__)
gtts(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    language = 'en'
    if request.method == 'POST':
        text = request.form['text']
        language = request.form['language']
        return render_template('index.html', result=text, s=language)
        #tts = gTTS(text=text, lang="en", tld=language)
        #audio_file = 'static/audio_output.mp3'
        #tts.save(audio_file)
        #return audio_file
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
