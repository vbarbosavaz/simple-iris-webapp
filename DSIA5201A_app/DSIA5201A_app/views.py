from DSIA5201A_app import app
from flask import Flask, request, render_template
import pickle
import pandas as pd

with open("DSIA5201A_app/static/ai/iris_classifier.pickle", "rb") as f:
    iris_classifier = pickle.load(f)

with open("DSIA5201A_app/static/ai/iris_classifier_features.pickle", "rb") as f:
    iris_classifier_features = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    flower = {}
    for feature in iris_classifier_features:
        flower[feature] = [request.form[feature]]

    flower = pd.DataFrame(flower)

    species = iris_classifier.predict(flower[iris_classifier_features])

    return render_template('index.html', prediction=species[0])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("403.html"), 403

@app.errorhandler(500)
def server_error_page(error):
    return render_template("500.html"), 500
