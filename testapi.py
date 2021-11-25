
import flask
import camera
from flask import request

app = flask.Flask(__name__)

#app.config["DEBUG"] = True
CORS(app)

defult_address = "/"
my_address = "/https://oooo2552.github.io/linguisticpuzzle/experiment.html"

@app.route('/')
def index():
    return "index page"

@app.route('/camera', methods=['GET'])
def start_camera():
    #if request.method == 'POST':
    #insert_values = request.get_json() 
    #filename = insert_values['subject']
    #filename = input("please enter the filename:")
    filename = "test_heroku"
    camera.main(filename)
    return "<h1>This is second camera for facial expression</h1>"


#app.run()