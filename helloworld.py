from flask import Flask,request
from pymongo import MongoClient
from bson.json_util import dumps
from flask_cors import CORS, cross_origin
# -*- coding: utf-8 -*-
app = Flask(__name__)
CORS(app)

@app.route('/fetchGraph',methods=['GET'])
def fetchGraph():
	client = MongoClient()
	db = client.facebook
	cursor = db.graphType.find({},{"_id":0})
	return dumps(cursor)

@app.route('/setup',methods=['POST','GET'])
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
	  },
	   {
	    "x": "Type",
	    "graph": "Pie"
	  },
	   {
	    "x": "Category",
	    "graph": "Pie"
	  },
	   {
	    "x": "Post Month",
	    "graph": "Pie"
	  },
	   {
	    "x": "Post Weekday",
	    "graph": "Pie"
	  }
	])



	result = db.ycoord.insert([{ 
		  "x":"Post Weekday",
		  "y":"share",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of posts that has been shared on particular days.Almost all the days have closely the same number of posts shared."
		},{ 
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who saw your Page post on each day.Seems like the number is almost same over each day."
		},{ 
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who clicked anywhere in your post on each day."
		},{ 
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of clicks anywhere in your post on each day."
		},
		{ 
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users engaged with your post on each day. Engagement includes any click or story created ."
		},
		{ 
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of times a post from your Page is displayed, whether the post is clicked on or not each day. People may see multiple impressions of the same post."
		},
		{ 
		  "x":"Post Weekday",
		  "y":"Total Interactions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the total interactions that includes the number of shares, likes and comments on each day."
		},{ 
		  "x":"Post Month",
		  "y":"share",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of posts that has been shared on each month."
		},{ 
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who saw your Page post on each month."
		},{ 
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who clicked anywhere in your post on each month."
		},{ 
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of clicks anywhere in your post each month."
		},
		{ 
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users engaged with your post each month. Engagement includes any click or story created ."
		},
		{ 
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of times a post from your Page is displayed, whether the post is clicked on or not each month. People may see multiple impressions of the same post."
		},
		{ 
		  "x":"Post Month",
		  "y":"Total Interactions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the total interactions that includes the number of shares, likes and comments each month."
		},
		{ 
		  "x":"Category",
		  "y":"share",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of posts that has been shared for each category."
		},{ 
		  "x":"Category",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who saw your Page post for each category."
		},{ 
		  "x":"Category",
		  "y":"Lifetime Post Consumers",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who clicked anywhere in your post for each category."
		},{ 
		  "x":"Category",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of clicks anywhere in your post for each category."
		},
		{ 
		  "x":"Category",
		  "y":"Lifetime Engaged Users",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users engaged with your post for each category.Engagement includes any click or story created."
		},
		{ 
		  "x":"Category",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of times a post from your Page is displayed, whether the post is clicked on or not for each category. People may see multiple impressions of the same post."
		},
		{ 
		  "x":"Category",
		  "y":"Total Interactions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the total interactions that includes the number of shares, likes and comments for each category."
		},{ 
		  "x":"Type",
		  "y":"share",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of posts that has been shared for each type"
		},{ 
		  "x":"Type",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Pie",
		  "text":"Pie Chart depicts depicts the number of unique users who saw your Page post for each type"
		},{ 
		  "x":"Type",
		  "y":"Lifetime Post Consumers",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users who clicked anywhere in your post  for each type"
		},{ 
		  "x":"Type",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of clicks anywhere in your post for each type"
		},
		{ 
		  "x":"Type",
		  "y":"Lifetime Engaged Users",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of unique users engaged with your post for each type.Engagement includes any click or story created."
		},
		{ 
		  "x":"Type",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the number of times a post from your Page is displayed, whether the post is clicked on or not  for each type. People may see multiple impressions of the same post."
		},
		{ 
		  "x":"Type",
		  "y":"Total Interactions",
		  "graph":"Pie",
		  "text":"Pie Chart depicts the total interactions that includes the number of shares, likes and comments for each type."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users who have seen the post that was posted in that particular day.There seems to be a peak on Tuesday and thursday meaning there are many users viewing that particular post on those days. "
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of times a post from users page is displayed though the post is clicked or not in that particular day.The line has a peak on thursday which seems to be interesting that at that time so many times a post appears in the users page."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users engaged with your post in that particular day. Engagement includes any click or story created.The line shows a peak on wednesday meaning that maximum unique users are engaged with your post on that day."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users who clicked anywhere in your post at that particular day of post and the line peaks on wednesday."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of clicks anywhere in your post in that particular post day."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of impressions just from people who have liked a page in that particular post day."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line",
		  "text":"Line chart depicts the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular post day."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line",
		  "text":"Line chart depicts the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular post day."
		},
		{ "x":"Post Weekday",
		  "y":"comment",
		  "graph":"Line",
		  "text":"Line chart depicts the number of comments on the publication per post day."
		},
		{ "x":"Post Weekday",
		  "y":"Total Interactions",
		  "graph":"Line",
		  "text":"Line chart depicts the sum of likes, comments, and shares of the post per post day"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users who have seen the post that was posted in that particular hour.There seems to be a peak at hour three meaning there are many users viewing that particular post at that time. "
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of times a post from users page is displayed though the post is clicked or not in that particular hour.The line has a peak at hour 3 which seems to be interesting that at that time so many times a post appears in the users page."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users engaged with your post in that particular hour. Engagement includes any click or story created.The line shows a peak at hour 3 meaning that maximum unique users are engaged with your post at that time."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users who clicked anywhere in your post at that particular hour of post and the line peaks at hour 3."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of clicks anywhere in your post in that particular post hour and the line peaks at hour 3."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of impressions just from people who have liked a page in that particular post hour."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line",
		  "text":"Line chart depicts the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular post hour."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line",
		  "text":"Line chart depicts the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular post hour."
		},
		{ "x":"Post Hour",
		  "y":"comment",
		  "graph":"Line",
		  "text":"Line chart depicts the number of comments on the publication per post hour."
		},
		{ "x":"Post Hour",
		  "y":"Total Interactions",
		  "graph":"Line",
		  "text":"Line chart depicts the sum of likes, comments, and shares of the post per post hour"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users who have seen the post that was posted in that particular month. "
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of times a post from users page is displayed though the post is clicked or not in that particular month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users engaged with your post in that particular month. Engagement includes any click or story created."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of unique users who clicked anywhere in your post at that particular month of post."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of clicks anywhere in your post in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Line",
		  "text":"Line chart depicts the total number of impressions just from people who have liked a page in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Line",
		  "text":"Line chart depicts the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Line",
		  "text":"Line chart depicts the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"comment",
		  "graph":"Line",
		  "text":"Line chart depicts the number of comments on the publication per Post Month."
		},
		{ "x":"Post Month",
		  "y":"Total Interactions",
		  "graph":"Line",
		  "text":"Line chart depicts the sum of likes, comments, and shares of the post per Post Month"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who have seen the post that was posted in that particular category"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram",
		  "text":" The histogram depict the total number of times a post from users page is displayed though the post is clicked or not in that particular category."
		},
		{ "x":"Category",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users engaged with your post in that particular category"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who clicked anywhere in your post at that particular category"
		},
		{ "x":"Category",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of clicks anywhere in your post in that particular category."
		},
		{ "x":"Category",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of impressions just from people who have liked a page in that particular category."
		},
		{ "x":"Category",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular category."
		},
		{ "x":"Category",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular category."
		},
		{ "x":"Category",
		  "y":"comment",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of comments on the publication per category."
		},
		{ "x":"Category",
		  "y":"Total Interactions",
		  "graph":"Histogram",
		  "text":"The histogram depict the sum of likes, comments, and shares of the post per category."
		},
		{ "x":"Category",
		  "y":"share",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of times the publication was shared per category."
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram",
		  "text":"The histogram depict the total amount paid for the number of unique users who have seen the post that was posted."
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram",
		  "text":" The histogram depict the total amount paid for the number of times a post from users page is displayed though the post is clicked or not."
		},
		{ "x":"Paid",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram",
		  "text":"The histogram depict the total amount paid for the number of unique users engaged with your post."
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram",
		  "text":"The histogram depict the total amount paid for the number of unique users who clicked anywhere in your post."
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram",
		  "text":"The histogram depict the total amount paid for the amount paid for the number of clicks anywhere in your post."
		},
		{ "x":"Paid",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the total amount paid for the number of impressions just from people who have liked a page."
		},
		{ "x":"Paid",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the amount paid for the number of people who saw a page postbecause they have liked that page (uniqueusers ) ."
		},
		{ "x":"Paid",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram",
		  "text":"The histogram depict the amount paid for the number of people who have liked a Page and clicked anywhere in a post (Unique users)."
		},
		{ "x":"Paid",
		  "y":"comment",
		  "graph":"Histogram",
		  "text":"The histogram depict the amount paid for the number of comments on the publication."},
		{ "x":"Paid",
		  "y":"Total Interactions",
		  "graph":"Histogram",
		  "text":"The histogram depict the amount paid for the sum of likes, comments, and shares of the post."
		},
		{ "x":"Paid",
		  "y":"share",
		  "graph":"Histogram",
		  "text":"The histogram depict the amount paid for the number of times the publication was shared."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who have seen the post that was posted in that particular Post Hour"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram",
		  "text":" The histogram depict the total number of times a post from users page is displayed though the post is clicked or not in that particular Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users engaged with your post in that particular Post Hour"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who clicked anywhere in your post at that particular Post Hour"
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of clicks anywhere in your post in that particular Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of impressions just from people who have liked a page in that particular Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"comment",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of comments on the publication per Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"Total Interactions",
		  "graph":"Histogram",
		  "text":"The histogram depict the sum of likes, comments, and shares of the post per Post Hour."
		},
		{ "x":"Post Hour",
		  "y":"share",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of times the publication was shared per Post Hour."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who have seen the post that was posted in that particular Post Month"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram",
		  "text":" The histogram depict the total number of times a post from users page is displayed though the post is clicked or not in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users engaged with your post in that particular Post Month"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who clicked anywhere in your post at that particular Post Month"
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of clicks anywhere in your post in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of impressions just from people who have liked a page in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular Post Month."
		},
		{ "x":"Post Month",
		  "y":"comment",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of comments on the publication per Post Month."
		},
		{ "x":"Post Month",
		  "y":"Total Interactions",
		  "graph":"Histogram",
		  "text":"The histogram depict the sum of likes, comments, and shares of the post per Post Month."
		},
		{ "x":"Post Month",
		  "y":"share",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of times the publication was shared per Post Month."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who have seen the post that was posted in that particular Post Weekday"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram",
		  "text":" The histogram depict the total number of times a post from users page is displayed though the post is clicked or not in that particular Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users engaged with your post in that particular Post Weekday"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who clicked anywhere in your post at that particular Post Weekday"
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of clicks anywhere in your post in that particular Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of impressions just from people who have liked a page in that particular Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"comment",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of comments on the publication per Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"Total Interactions",
		  "graph":"Histogram",
		  "text":"The histogram depict the sum of likes, comments, and shares of the post per Post Weekday."
		},
		{ "x":"Post Weekday",
		  "y":"share",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of times the publication was shared per Post Weekday."
		},
		{ "x":"Type",
		  "y":"Lifetime Post Total Reach",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who have seen the post that was posted in that particular Type"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Total Impressions",
		  "graph":"Histogram",
		  "text":" The histogram depict the total number of times a post from users page is displayed though the post is clicked or not in that particular Type."
		},
		{ "x":"Type",
		  "y":"Lifetime Engaged Users",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users engaged with your post in that particular Type"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Consumers",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of unique users who clicked anywhere in your post at that particular Type"
		},
		{ "x":"Type",
		  "y":"Lifetime Post Consumptions",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of clicks anywhere in your post in that particular Type."
		},
		{ "x":"Type",
		  "y":"Lifetime Post Impressions by people who have liked your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the total number of impressions just from people who have liked a page in that particular Type."
		},
		{ "x":"Type",
		  "y":"Lifetime Post reach by people who like your Page",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who saw a page postbecause they have liked that page (uniqueusers ) in that particular Type."
		},
		{ "x":"Type",
		  "y":"Lifetime People who have liked your Page and engaged with your post",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of people who have liked a Page and clicked anywhere in a post (Unique users) in that particular Type."
		},
		{ "x":"Type",
		  "y":"comment",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of comments on the publication per Type."
		},
		{ "x":"Type",
		  "y":"Total Interactions",
		  "graph":"Histogram",
		  "text":"The histogram depict the sum of likes, comments, and shares of the post per Type."
		},
		{ "x":"Type",
		  "y":"share",
		  "graph":"Histogram",
		  "text":"The histogram depict the number of times the publication was shared per Type."
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
		  "graph":"Scatter Plot",
		  "text":"Scatter plot depicts two plots.First depicts the points of particular day of a month and second depicts points of post for which amount is paid on that day."
		},
		{ "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Paid",
		  "graph":"Scatter Plot",
		  "text":"Scatter plot depicts two plots.First depicts the points of particular hour of month and second depicts points of posts for which amount is paid in that hour."
		},
		{ "x":"Post Weekday",
		  "y":"Post Hour",
		  "z":"Paid",
		  "graph":"Scatter Plot",
		  "text":"Scatter plot depicts two plots.First depicts the points of particular hour of the day and second depicts points of posts for which amount is paid in that hour."
		},
		{ "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Category",
		  "graph":"Scatter Plot",
		  "text":"Scatter plot depicts two plots.First depicts the points of particular day on the month and second depicts points of posts of a category posted in that week."
		},
		{ "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Category",
		  "graph":"Scatter Plot",
		  "text":"Scatter plot depicts two plots.First depicts the points of particular hour of the month and second depicts points of posts of a category posted in that hour."
		},
		{ "x":"Post Weekday",
		  "y":"Post Hour",
		  "z":"Category",
		  "graph":"Scatter Plot",
		  "text":"Scatter plot depicts two plots.First depicts the points of particular day of the week and second depicts points of posts of a category posted in that hour."
		},
		{
		  "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Category",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total number of posts on a particular hour of the month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Post Hour",
		  "z":"Paid",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total amount paid for the posts on a particular hour of the month."
		},
		{
		  "x":"Post Month",
		  "y":"Post Hour",
		  "z":"comment",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total number of comments on a particular hour of the month."
		},
		{
		  "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Category",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total number of posts on a particular day of the month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"Paid",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total amount paid for the posts on a particular day of the month."
		},
		{
		  "x":"Post Month",
		  "y":"Post Weekday",
		  "z":"comment",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total number of comments on a particular day of the month."
		},
		{
		  "x":"Post Hour",
		  "y":"Post Weekday",
		  "z":"Category",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total number of posts on a particular hour of the day grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Post Weekday",
		  "z":"Paid",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total amount paid for the posts on a particular hour of the day."
		},
		{
		  "x":"Post Hour",
		  "y":"Post Weekday",
		  "z":"comment",
		  "graph":"Heat Map",
		  "text":"The heatmap depicts that the total number of comments on a particular hour of the day grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular month grouped by Type."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Reach",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular month grouped by paid."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular month grouped by Type."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular month grouped by paid"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular month grouped by type."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that depicts that the total number of unique users engaged with your post in particular month grouped by paid"
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Engaged Users",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that depicts that the total number of unique users engaged with your post in particular month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular month grouped by type."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumers",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular month grouped by paid."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular month grouped by type."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post Consumptions",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular month grouped by paid."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular month grouped by type."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular month grouped by category."
		},
		{
		  "x":"Post Month",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular month grouped by paid."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular hour grouped by Type."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Reach",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular hour grouped by paid."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular hour grouped by type."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular hour grouped by paid."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular hour grouped by type."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Engaged Users",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular hour grouped by type."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumers",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular hour grouped by paid."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular hour grouped by type."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post Consumptions",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular hour grouped by paid."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular hour grouped by type."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular hour grouped by category."
		},
		{
		  "x":"Post Hour",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular hour grouped by paid."
		},
			{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular day grouped by Type."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Reach",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who have seen the post that was posted in particular day grouped by paid."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular day grouped by type."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Total Impressions",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of times a post from users page is displayed though the post is clicked or not in particular day grouped by paid."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular day grouped by type."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Engaged Users",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users engaged with your post in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular day grouped by type."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumers",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of unique users who clicked anywhere in your post in particular day grouped by paid."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular day grouped by type."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post Consumptions",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of clicks anywhere in your post in particular day grouped by paid."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Type",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular day grouped by type."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Category",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular day grouped by category."
		},
		{
		  "x":"Post Weekday",
		  "y":"Lifetime Post reach by people who like your Page",
		  "z":"Paid",
		  "graph":"Multi Scatter",
		  "text":"The multiscatter plot depicts that the total number of impressions just from people who have liked a page in particular day grouped by paid."
		}])
	cursor = db.xcoord.find({},{"_id":0})
	return dumps(cursor)

@app.route('/fetchxCoordinates',methods=['GET'])
def fetchxCoordinates():
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	cursor = db.xcoord.find({"graph":graphTypeVal},{"_id":0})
	return dumps(cursor)


@app.route('/fetchyCoordinates',methods=['GET'])
def fetchyCoordinates():
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	xCordVal = request.args.get('xCoord')
 
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

@app.route('/fetchxyText',methods=['GET'])
def fetchxyText():
	print('tttt');
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	xCordVal = request.args.get('xCoord')
	yCordVal = request.args.get('yCoord')
	cursor = db.ycoord.find({"graph":graphTypeVal,"x":xCordVal,"y":yCordVal},{"graph":0,"x":0,"y":0,"_id":0})
	return dumps(cursor)


@app.route('/fetchxyzText',methods=['GET'])
def fetchxyzText():
	print('tttt');
	client = MongoClient()
	db = client.facebook
	graphTypeVal = request.args.get('graphType')
	xCordVal = request.args.get('xCoord')
	yCordVal = request.args.get('yCoord')
	zCordVal = request.args.get('zCoord')
	cursor = db.zcoord.find({"graph":graphTypeVal,"x":xCordVal,"y":yCordVal,"z":zCordVal},{"graph":0,"x":0,"y":0,"z":0,"_id":0})
	return dumps(cursor)



if __name__ == '__main__':
      app.run(host="128.119.243.168",port=18000,debug="true",threaded="true")