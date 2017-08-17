from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from string import Template
from random import randint
import json
import pymongo
import requests
import datetime
import time
import urlparse
import hashlib as hl
import os
import httpagentparser

from extra_methods import *


app = Bottle(__name__)



client = MongoClient('mongodb://els:hack123@34.228.79.24:27017/els')
db = client.els


@app.route('/')
def root():
	return template('index')


@app.get('/els_setup/<email>')
def els_setup(email):
	cur = db.emp.find({'email': email})
	data = json.loads(dumps(cur))

	return template('els_setup', info=data[0])

@app.get('/els_setup_status/<email>/<fp>')
def els_setup_status(email, fp):

	cur = db.emp.find({'email': email})
	data = json.loads(dumps(cur))

	if(len(data[0]['fp']) == 0 and data[0]['status'] == 0):
		cur = db.emp.update({'email': email},{'$set': {'fp': fp, 'status': 1}})
		return template('els_setup_status', info={'status': 'Success'})
	else:
		return template('els_setup_status', info={'status': 'Error'})

@app.get('/log/<email>/<fp>')
def log(email, fp):

	cur = db.emp.find({'email': email})
	data = json.loads(dumps(cur))

	if(len(data) != 0):
		if(data[0]['fp'] == fp and data[0]['status'] == 1):
			cur = db.logs.find({"email": email}).sort('_id',pymongo.DESCENDING).limit(1)
			data_1 = json.loads(dumps(cur))

			if(len(data_1) != 0):
				if(len(data_1) != 0 and data_1[0]['log_in_status'] == 1 and data_1[0]['log_out_status'] == 0):
					res = compare_date(data_1[0]['log_in_time_stamp'], time.time())
					if(res == 1):
						cur = db.logs.update({'_id': data_1[0]['_id']}, {'$set':{'log_out_time_stamp': time.time(), 'log_out_status': 1}})
						return 'Logged Out'
					elif(res == 0 or res == -1):
						cur = db.logs.insert({'email': email,'fp': fp,'log_in_status': 1,'log_out_status': 0,'log_in_time_stamp': time.time(),'log_out_time_stamp': ''})
						return 'Logged In'
					else:
						return 'Error 1'
				elif(len(data_1) != 0 and data_1[0]['log_out_status'] == 1):
					res = compare_date(data_1[0]['log_in_time_stamp'], time.time())
					if(res == 1):
						return 'Logged Out'
					elif(res == 0 or -1):
						cur = db.logs.insert({'email': email,'fp': fp,'log_in_status': 1,'log_out_status': 0,'log_in_time_stamp': time.time(),'log_out_time_stamp': ''})
						return 'Logged In'
			else:
				cur = db.logs.insert({'email': email,'fp': fp,'log_in_status': 1,'log_out_status': 0,'log_in_time_stamp': time.time(),'log_out_time_stamp': ''})
				return 'Logged In'
		elif(data[0]['fp'] == fp and data[0]['status'] == 0):
			return 'Error 3'
	else:
		return 'Error 4'
			# if(len(data_1) != 0):
				# last_date = datetime.datetime.fromtimestamp(int(data_1).strftime('%Y-%m-%d')

			# if(len(data_1) != 0 and data_1[0]['log_in_status'] == 1):
			# 	last_date = datetime.datetime.fromtimestamp(int(data_1).strftime('%Y-%m-%d')
			# 	return 'Done'
			# elif(len(data_1) != 0 and data_1[0]['log_out_status'] == 0):
			# 	last_date_1 = datetime.datetime.fromtimestamp(int(data_1).strftime('%Y-%m-%d')
			# elif(len(data_1) != 0 and data_1[0]['log_out_status'] == 1):
			# 	last_date = datetime.datetime.fromtimestamp(int(data_1).strftime('%Y-%m-%d')



# Static Routes
@app.route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='')

@app.route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='')

@app.route('/<filename:re:.*\.(jpg|png|gif|ico|svg)>')
def images(filename):
    return static_file(filename, root='')

@app.route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='')

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'