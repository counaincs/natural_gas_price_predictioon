from flask import Flask, request, render_template
import requests
from joblib import load
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/businessv')
def businessv():
    return render_template('businessv.html')

@app.route('/algused')
def algused():
    return render_template('algused.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


if __name__ == "__main__":
    app.run(debug=True)
