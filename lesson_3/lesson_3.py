from pymongo import MongoClient
from lesson2 import hh,superjob
import pandas as pd
import json
from pprint import pprint


client = MongoClient('mongodb://moriska32:6841539@192.168.40.129:27017')

def morethen(then, where):

	db = client[where]
	docs = db.docs
	objects = docs.find({"salary_min":{'$gt':then}})

	result = []
	for obj in objects:
		result.append(obj)
	return result
def insert(where, pool):
	db = client[where]
	docs = db.docs
	records = json.loads(pool.T.to_json()).values()
	result = docs.insert_many(records)


def update(where, items,record):
	db = client[where]
	docs = db.docs
	objects = docs.find({'link':items}).count()
	if objects == 0:
		docs.insert_one(record)
	else:
		docs.update({'link':items},record)
	
	


search_str="python"
n_str=2

a = pd.DataFrame(hh('https://hh.ru',search_str,n_str))
#b = pd.DataFrame(superjob('https://www.superjob.ru',search_str,n_str))

records = json.loads(a.T.to_json()).values()
for items in records:
	update("hh",items['link'],items)


pprint(morethen(100000, "hh"))
