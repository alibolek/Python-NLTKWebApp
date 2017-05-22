# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords #stopwords
from nltk.tokenize import word_tokenize #tokenize
from nltk.stem.snowball import SnowballStemmer #stemming
from nltk.corpus import state_union #part of speech
from nltk.corpus import wordnet as wn


def tokenizer():
	
	if len(request.vars)!=0:
		user_input=request.vars
		import sys
		reload(sys)
		sys.setdefaultencoding('utf-8')
		if user_input.parameter=="sentence":
			our_output=nltk.sent_tokenize(user_input.input,"turkish")
		else:
			our_output=nltk.word_tokenize(user_input.input,"turkish")
		user_input.output=our_output
	return locals()


def stop_words():
	if len(request.vars)!=0:
		import sys
		reload(sys)
		sys.setdefaultencoding('utf-8')
		user_input=request.vars
		last=[]
		if user_input.parameter=="turkish":
			stop_words=set(stopwords.words("turkish"))
			tokenized=word_tokenize(user_input.input,'turkish')
		else:
			stop_words=set(stopwords.words("english"))
			tokenized=word_tokenize(user_input.input,'english')
		for w in tokenized:
			if w not in stop_words:
				last.append(w)
		
		
	return locals()

def stemming():
	if len(request.vars)!=0:
		user_input=request.vars
		tokenized=word_tokenize(user_input.input,'english')
		stemmer = SnowballStemmer("english")
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
	import sentiment
	from sentiment import runtweets
	from sentiment import classifier
	from sentiment import *
	if len(request.vars)!=0:
		user_input=request.vars
		runtweets.append(user_input.input)
		poscount = 0
		negcount = 0
		for tweett in runtweets:
		  valued = classifier.classify(extract_features(tweett.split()))
		  print (valued)
		  if valued == 'negative':
		    negcount = negcount + 1
		  else:
		    poscount = poscount + 1
		    print ('Positive count: %s \nNegative count: %s' % (poscount,negcount))