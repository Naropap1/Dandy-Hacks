import calc, parse

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
        times = json.loads(request.data.decode('utf-8'))
        #print(times)
        #data = json.loads(''.join(times))
        #print(data)
        #data = cgi.FieldStorage()
        #times2 = json.loads(data[times].value)
        #print(times2)
        print(times[0])
        print(times[1])
        values = calc.daily_naps(parse.findOccupied(times), parse.calcMinutes(times[1]), parse.calcMinutes(times[0]), 0) #add any other parameters
        #print(values)
        return "foo"
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

