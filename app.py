# Below we import the flask module
from flask import *

# below  we create a flask application
app = Flask(__name__)

# below we have a home route
# We use a decorator to create routes on flask
@app.route("/home")
def home():
    return "Welcome to the home URL"


@app.route("/about")
def about():
    return "Welcome to the about URL"

# create two additional routes i.e contact and products. Render a simple response on the the browser


# run the application
app.run(debug = True)