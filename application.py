"""Code to run the Flask Server"""

# Importing dependencies
from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
import math
import johnsonsAlgorithm as JA

# Creating the app to run
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/demo", methods=["POST", "GET"])
def demo():

    # Only to go to the page
    if request.method == 'GET':

        # render the demo page
        return render_template("demo.html")

    # File has been validated and needed to be processed
    elif request.method == 'POST':
        
        # Extracting data from demo page
        num = int(request.form.get("nodeNum"))

        # Getting source nodes
        source = request.form.getlist("source[]")
        source = list(map(int, source))

        # Getting destination nodes
        destination = request.form.getlist("destination[]")
        destination = list(map(int, destination))

        # Getting weights for source, destination pair
        weights = request.form.getlist("weight[]")

        # Enumerating to modify the data 
        for i, j in enumerate(weights):

            if (j == "infinity"):

                # Converting "infinity" to math.inf
                weights[i] = math.inf
                
        weights = list(map(float, weights))

        # Creating adjacency matrix from extracted data
        adjMatrix = np.full([num, num], math.inf)

        # Adding the values to the adjacency matrix
        for i, j, k in zip(source, destination, weights):
            adjMatrix[i, j] = k

        # Passing the adjacency matrix to Johnson's Algorithm
        JA.Johnson(adjMatrix)

        # rendering the result html page for results using matplotlib images
        return render_template("result.html")

@app.errorhandler(404)
def page_not_found(e):

    # Error page if invalid URL entered
    return render_template("error.html"), 404