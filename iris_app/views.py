from datetime import datetime
import os

from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import LogisticRegression

import pickle

import sys
print(sys.version)

from . import app

@app.route("/")
def home():
    return render_template("home.html")

# Example request http://127.0.0.1:5000/api/iris?sepal_length=5&sepal_width=3&petal_length=4&petal_width=1
@app.route("/api/iris/")
def iris():
    s_length = request.args.get("sepal_length")
    s_width = request.args.get("sepal_width")
    p_length = request.args.get("petal_length")
    p_width = request.args.get("petal_width")

    if(s_length == None or s_width == None or p_length == None or p_width == None):
        return "Parameters not entered"

    s_length_val = float(s_length)
    s_width_val = float(s_width)
    p_length_val = float(p_length)
    p_width_val = float(p_width)

    directory = os.path.dirname(os.path.abspath(__file__))
    ml_model = pickle.load(open(directory + "/ml_model/iris_regression_model.sav", "rb"))
    prediction = ml_model.predict([[s_length_val, s_width_val, p_length_val, p_width_val]])[0]
    if(prediction == 0):
        return jsonify(species="Setosa")
    elif(prediction == 1):
        return jsonify(species="Versicolor")
    elif(prediction == 2):
        return jsonify(species="Virginica")
    else:
        return jsonify(species="Unknown")
        