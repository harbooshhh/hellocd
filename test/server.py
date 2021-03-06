
"""
main module of the server file
"""

# 3rd party moudles
from flask import render_template,jsonify


# local modules
import config
import people

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger3.yaml")


# create a URL route in our application for "/"
@connex_app.route("/")


@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(debug=True,port=3010)

