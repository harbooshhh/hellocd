
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
connex_app.add_api("swagger2.yml")


# create a URL route in our application for "/"
@connex_app.route("/")
"""
def home():
   
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
   
    
    #return render_template("home.html")
    #return "heloo there...."
    return jsonify(people.read_all())

##@app.route('/user', methods=['GET'])

#@connex_app.route('/person', methods=['GET'])
def Get_all_Person():
    return jsonify(people.read_all())


@connex_app.route("/person/<ThinkId>",methods['GET'])
def GetPerson(ThinkId):
    return jsonify(people.read_one(ThinkId))
"""

if __name__ == "__main__":
    connex_app.run(debug=True)

