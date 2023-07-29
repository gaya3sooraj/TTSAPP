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
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
