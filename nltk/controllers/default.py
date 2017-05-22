# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import stopwords #stopwords
from nltk.tokenize import word_tokenize,sent_tokenize #tokenize
from nltk.stem.snowball import SnowballStemmer #stemming
from nltk.stem.porter import *
from nltk.corpus import state_union #part of speech
from nltk.corpus import wordnet as wn
from nltk.sentiment.vader import SentimentIntensityAnalyzer

	
def index():
	
	return locals()

def tokenizer():
	if len(request.vars)!=0:
		user_input=request.vars
		import sys
		reload(sys)
		sys.setdefaultencoding('utf-8')
		if user_input.parameter=="sentence":
			
			our_output=nltk.sent_tokenize(user_input.input,"english")
			print user_input
			if request.vars.filename!='' and len(request.vars.filename.value)!="":
				file_input=user_input.filename.value
				file_output=nltk.word_tokenize(file_input,"english")
			print our_output
		else:
			our_output=nltk.word_tokenize(user_input.input,"english")
			if request.vars.filename!='' and len(request.vars.filename.value)!=None:
				file_input=user_input.filename.value
				file_output=nltk.word_tokenize(file_input,"english")
			
			
		user_input.output=our_output
		

	return locals()

def stop_words():
	if len(request.vars)!=0:
		import sys
		reload(sys)  
		sys.setdefaultencoding('utf8')
		user_input=request.vars
		last=[]
		print stopwords.words()
		if user_input.parameter=="turkish":
			stop_words=set(stopwords.words("turkish"))
			tokenized=word_tokenize(user_input.input,'turkish')
		else:
			stop_words=set(stopwords.words("english"))
			tokenized=word_tokenize(user_input.input,'turkish')
		for w in tokenized:
			if w in stop_words:
				last.append(w)
		print last
	return locals()

def stemming():
	if len(request.vars)!=0:
		user_input=request.vars
		tokenized=word_tokenize(user_input.input,'english')
		if user_input.parameter=="snowball":
			stemmer = SnowballStemmer("english")
			print " ".join(SnowballStemmer.languages)
		else:
			stemmer = PorterStemmer()
			
		last=[]
		for w in tokenized:
			last.append(stemmer.stem(w))
		
	return locals()

def part_of_speech():
	if len(request.vars)!=0:
		user_input=request.vars
		
		tokenized=word_tokenize(user_input.input,"english")
		tag_list=[]
		try:
			tagged=nltk.pos_tag(tokenized)
			for t in tagged:
				tag_list.append(t)
			print tag_list
		except Exception as e:
			print str(e)
	return locals()

def meaning():
	if len(request.vars)!=0:
		user_input=request.vars
		#tokenized=word_tokenize(user_input.input,"english")
		synset=wn.synsets(user_input.input)	
	return locals()

def sentiment_analyse():
	if len(request.vars)!=0:
		user_input=request.vars
		tokenized=sent_tokenize(user_input.input,"english")
		sid = SentimentIntensityAnalyzer()
		if request.vars.filename!='' and len(request.vars.filename.value)!="":
			print request.vars.filename.value
			file_input=user_input.filename.value
			file_output_sent=nltk.sent_tokenize(file_input,"english")
	return locals()
	
def contact():
	user_input=request.vars
	if user_input.input=="To See Contact Information Execute Me :)":
		output="**Project Owner: Muhammed Ali Bolek \n**Mail:muhammedalibolek@gmail.com \n**Project Instructor:Bekir Taner Dinçer(Phd.)"
	else:output="This is not correct text to see contact information"
	return locals()


def user():
	"""
	exposes:
	http://..../[app]/default/user/login
	http://..../[app]/default/user/logout
	http://..../[app]/default/user/register
	http://..../[app]/default/user/profile
	http://..../[app]/default/user/retrieve_password
	http://..../[app]/default/user/change_password
	http://..../[app]/default/user/bulk_register
	use @auth.requires_login()
		@auth.requires_membership('group name')
		@auth.requires_permission('read','table name',record_id)
	to decorate functions that need access control
	also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
	"""
	return dict(form=auth())


@cache.action()
def download():
	"""
	allows downloading of uploaded files
	http://..../[app]/default/download/[filename]
	"""
	return response.download(request, db)


def call():
	"""
	exposes services. for example:
	http://..../[app]/default/call/jsonrpc
	decorate with @services.jsonrpc the functions to expose
	supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
	"""
	return service()


