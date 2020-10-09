"""Code to run the Flask Server"""

# Importing dependencies
from flask import Flask, render_template, request, redirect, url_for, jsonify

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

        # validation of the received form
        # rendering the result html page for results using matplotlib images
        return render_template("result.html")

@app.errorhandler(404)
def page_not_found(e):

    # Error page if invalid URL entered
    return render_template("error.html"), 404