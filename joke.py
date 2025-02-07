import pyjokes
from flask import Flask, render_template_string

app = Flask(__name__)

def get_random_joke():
    return pyjokes.get_joke()

@app.route('/')
def home():
    joke = get_random_joke()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Random Joke Generator</title>
        </head>
        <body>
            <h1>Random Programming Joke</h1>
            <p>{{ joke }}</p>
            <button onclick="window.location.reload();">Get Another Joke</button>
        </body>
        </html>
    ''', joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
