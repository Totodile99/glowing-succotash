# Import Libraries
import os
from flask import Flask, flash, request, redirect, url_for, render_template

# Initilize the Flask
app = Flask(__name__)
@app.route('/')

# Route and define the index function to render the home.html.
def index():
	return render_template('index.html')



# Call the app.run()
if __name__ == "__main__":
	app.run()

