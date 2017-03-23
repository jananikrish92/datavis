from flask import Flask,request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/fetchGraph')
def fetchGraph():
	client = MongoClient()
	db = client.facebook
	cursor = db.graphType.find({},{"graph":1,"_id":0})
	return dumps(cursor)


@app.route('/setup')
def setUp():
	client = MongoClient()
	db = client.facebook
	db.coordinateGraph.remove()
	db.graphType.remove()
	result = db.graphType.insert([
	    {"graph": "Scatter Plot"},
	    {"graph": "Line"},
	    {"graph": "Heat Map"},
	    {"graph": "Histogram"},
	     {"graph": "Multiscatter"},
	      {"graph": "Pie"}
	])
	result = db.coordinateGraph.insert([
		{"x":"Post Month","y":"Post Weekday","z":"Paid","graph":"Scatter Plot"},{"x":"Post Month","y":"Lifetime Post Total Reach","graph":"Line"},
		{"x":"like","y":"Category","graph":"Histogram"},{"x":"Post Month","y":"Post Hour","z":"Paid","graph":"Heat Map"},{"x":"Post Month","y":"Lifetime Post Consumers","z":"Type","graph":"Multiscatter"},{"x":"Type","y":"share","graph":"Pie"}])
	cursor = db.coordinateGraph.find({},{"_id":0})
	return "setup completed"

@app.route('/fetchCoordinates')
def fetchCoordinates():
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	print(graphTypeVal)
	cursor = db.coordinateGraph.find({"graph":graphTypeVal},{"_id":0})
	return dumps(cursor)


if __name__ == '__main__':
   app.run()
