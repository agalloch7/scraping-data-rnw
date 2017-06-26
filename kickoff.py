import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
import time
import pandas as pd
import langid
import glob
import os
from pymongo import MongoClient
from classes.business import Business

def read_data():
	"""
	INPUT: None
	OUTPUT: pandas data frame from file
	"""
	''
	list_of_files = glob.glob('uploads/*.csv') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	df = pd.read_csv(latest_file)
	df_filter = df[df['comment_author'] != 'Love Matters Africa']
	return df_filter


def filter_date (start_date, end_date, df):

	df['comment_published'] = pd.to_datetime(df['comment_published'])  
	mask = (df['comment_published'] > start_date) & (df['comment_published'] <= end_date)
	df = df.loc[mask]

	return df

def filter_language (df):
	df['lang'] = ''
	df['prob'] = ''

	for index, row in df.iterrows():
		df['lang'][index], df['prob'][index] = langid.classify(row['comment_message'])

	return df[df.lang == 'en']

def run_kickoff(start_date, end_date): 

	client = MongoClient()
	db = client.rnwtest2
	summaries_coll = db.summaries	

	print "Loading data..."
	df = read_data()

	biz = Business(filter_date(start_date, end_date, df))

	start = time.time()

	summary = biz.aspect_based_summary()
		
	summaries_coll.insert(summary, check_keys=False)

	print "Inserted summary for %s into Mongo" % biz.business_name

	elapsed = time.time() - start
	print "Time elapsed: %d" % elapsed


if __name__ == "__main__":
	run_kickoff(start_date, end_date)



