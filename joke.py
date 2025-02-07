import pyjokes
from flask import Flask, render_template

app = Flask(__name__)

def get_random_joke():
    return pyjokes.get_joke()

@app.route('/')
def home():
    joke = get_random_joke()
    return render_template('index.html', joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
