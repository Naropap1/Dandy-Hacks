
from flask import Flask, render_template, request, jsonify
import json
import cgitb
import cgi
cgitb.enable()

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template("index.html");



@app.route('/naps', methods = ['GET','POST'])
def getNap():
    if request.method == 'POST':
        print("A")
        times = json.loads(request.data.decode('utf-8'))
        print(times)
        values = '{begin:"12:00 AM",end:"12:05 AM"}' #add any other parameters
        print("C")
        return jsonify(results = values)

if __name__ == "__main__":
    app.run(debug=True)
	

#class JSONInterface(webapp2.RequestHandler):
   # def post(self):
   #     callback = self.request.get('callback')
   #     logging.info(callback) # will print correctly
   #     self.response.out.write(json.dumps(callback)) 


data = cgi.FieldStorage()
times = json.loads(data["times"].value)

