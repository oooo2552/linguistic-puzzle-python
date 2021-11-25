from app import app ##
import flask
import camera
from flask import request

#app = flask.Flask(__name__)
#app.config["DEBUG"] = True


#defult_address = "/"
#my_address = "/https://oooo2552.github.io/linguisticpuzzle/experiment.html"

@app.route('/')
def index():
    return "index page"

@app.route('/camera', methods=['GET','POST'])
def start_camera():
    if request.method == 'POST':
      insert_values = request.get_json() 
      filename = insert_values['subject']
    else:
      #filename = input("please enter the filename:")
      filename = "test3"
    camera.main(filename)
    return "<h1>This is second camera for facial expression</h1>"


#app.run()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
