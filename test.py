import sys
import nltk

data = r'data/sample.txt'

with open(data,"r") as f:
	for ln in f:
		# print(ln)
		token = nltk.word_tokenize(ln)
		print(token)