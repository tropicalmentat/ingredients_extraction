import sys
import nltk

data = r'data/sample.txt'

with open(data,"r") as f:
	for ln in f:
		token = nltk.word_tokenize(ln)
		pos = nltk.pos_tag(token)

		nouns = [wd[0] for wd in pos if wd[1]=="NN" or wd[1]=="NNS"]

		print(nouns)