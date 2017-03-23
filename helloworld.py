from flask import Flask,request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/fetchGraph',methods=['GET'])
def fetchGraph():
	client = MongoClient()
	db = client.facebook
	cursor = db.graphType.find({},{"_id":0})
	return dumps(cursor)

@app.route('/setup',methods=['POST'])
def setUp():
	client = MongoClient()
	db = client.facebook
	db.xcoord.remove()
	db.ycoord.remove()
	db.zcoord.remove()
	db.graphType.remove()
	result = db.graphType.insert([
	     {"graph": "Scatter Plot"},
	     {"graph": "Line"},
	     {"graph": "Heat Map"},
	     {"graph": "Histogram"},
	     {"graph": "Multi Scatter"},
	     {"graph": "Pie"}
	 ])

	result = db.xcoord.insert([{
	    "x": "Post Month",
	    "graph": "Scatter Plot"
	  },
	  {
	    "x": "Post Weekday",
	    "graph": "Scatter Plot"
	  },
	  {
	    "x": "Post Month",
	    "graph": "Multi Scatter"
	  },
	  {
	    "x": "Post Weekday",
	    "graph": "Multi Scatter"
	  },
	  {
	    "x": "Post Hour",
	    "graph": "Multi Scatter"
	  },
	  {
	    "x": "Post Month",
	    "graph": "Heat Map"
	  },
	  {
	    "x": "Post Hour",
	    "graph": "Heat Map"
	  },
	  {
	    "x": "Type",
	    "graph": "Histogram"
	  },
	  {
	    "x": "Paid",
	    "graph": "Histogram"
	  },
	  {
	    "x": "Category",
	    "graph": "Histogram"
	  },
	  {
	    "x": "Post Hour",
	    "graph": "Histogram"
	  },
	  {
	    "x": "Post Month",
	    "graph": "Histogram"
	  },
	  {
	    "x": "Post Weekday",
	    "graph": "Histogram"
	  },
	  {
	    "x": "Lifetime Post Total Reach",
	    "graph": "Line"
	  },
	  {
	    "x": "Post Hour",
	    "graph": "Line"
	  },
	  {
	    "x": "Post Month",
	    "graph": "Line"
	  },
	  {
	    "x": "Post Weekday",
	    "graph": "Line"
	  }
	])



	result = db.ycoord.insert([{ 
		  "x":"Lifetime Post Total Reach",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"comment",
		  "graph":"Line"
		},
		{ "x":"Lifetime Post Total Reach",
		  "y":"Total Interactions",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"comment",
		  "graph":"Line"
		},
		{ "x":"Post Weekday",
		  "y":"Total Interactions",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"comment",
		  "graph":"Line"
		},
		{ "x":"Post Hour",
		  "y":"Total Interactions",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"comment",
		  "graph":"Line"
		},
		{ "x":"Post Month",
		  "y":"Total Interactions",
		  "graph":"Line"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"comment",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"Total Interactions",
		  "graph":"Histogram"
		},
		{ "x":"Category",
		  "y":"share",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"comment",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"Total Interactions",
		  "graph":"Histogram"
		},
		{ "x":"Paid",
		  "y":"share",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"comment",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"Total Interactions",
		  "graph":"Histogram"
		},
		{ "x":"Post Hour",
		  "y":"share",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"comment",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Total Interactions",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"share",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"comment",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"Total Interactions",
		  "graph":"Histogram"
		},
		{ "x":"Post Weekday",
		  "y":"share",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"comment",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"Total Interactions",
		  "graph":"Histogram"
		},
		{ "x":"Type",
		  "y":"share",
		  "graph":"Histogram"
		},
		{ "x":"Post Month",
		  "y":"Post Weekday",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Month",
		  "y":"Post Hour",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Weekday",
		  "y":"Post Hour",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Multi Scatter"
		},
		{ "x":"Post Month",
		  "y":"Post Hour",
		  "graph":"Heat Map"
		},
		{ "x":"Post Month",
		  "y":"Post Weekday",
		  "graph":"Heat Map"
		},
		{ "x":"Post Hour",
		  "y":"Post Weekday",
		  "graph":"Heat Map"
		}
		])

	result = db.zcoord.insert([
		{ "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Paid",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Paid",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Weekday",
		  "y":"Post Hour",
		  "z":"Paid",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Category",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Category",
		  "graph":"Scatter Plot"
		},
		{ "x":"Post Weekday",
		  "y":"Post Hour",
		  "z":"Category",
		  "graph":"Scatter Plot"
		},
		{
		  "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Category",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Paid",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Month",
		  "y":"Post Hour",
		  "z":"comment",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Category",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Paid",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"comment",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Hour",
		  "y":"Post Weekday",
		  "z":"Category",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Hour",
		  "y":"Post Weekday",
		  "z":"Paid",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Hour",
		  "y":"Post Weekday",
		  "z":"comment",
		  "graph":"Heat Map"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "z":"Category",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Type",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Paid",
		  "graph":"Multi Scatter"
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Category",
		  "graph":"Multi Scatter"
	}])
	cursor = db.xcoord.find({},{"_id":0})
	return dumps(cursor)

@app.route('/fetchxCoordinates',methods=['GET'])
def fetchxCoordinates():
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	print graphTypeVal
	cursor = db.xcoord.find({"graph":graphTypeVal},{"_id":0})
	return dumps(cursor)


@app.route('/fetchyCoordinates',methods=['GET'])
def fetchyCoordinates():
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	xCordVal = request.args.get('xCoord')
 	
	print xCordVal;
	cursor = db.ycoord.find({"graph":graphTypeVal,"x":xCordVal},{"_id":0})
	return dumps(cursor)



@app.route('/fetchzCoordinates',methods=['GET'])
def fetchzCoordinates():
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	xCordVal = request.args.get('xCoord')
	yCordVal = request.args.get('yCoord')
	cursor = db.zcoord.find({"graph":graphTypeVal,"x":xCordVal,"y":yCordVal},{"graph":0,"x":0,"y":0,"_id":0})
	return dumps(cursor)

if __name__ == '__main__':
   app.run()
