import nltk
from nltk.corpus import stopwords

data_fpath = r'data/sample.txt'
corpus_fpath = r'data/corpora.txt'

with open(corpus_fpath,"r") as stop:

	cook_stop = [wd.strip('\n') for wd in stop.readlines()]


with open(data_fpath,"r") as rcp:
	for ln in rcp:
		token = nltk.word_tokenize(ln)

		filtered = [wd for wd in token if wd not in cook_stop]

		pos = nltk.pos_tag(filtered)

		nouns = [wd[0] for wd in pos if wd[1]=="NN" or wd[1]=="NNS"]
		
		print(nouns)

		# TODO: handle fractions by filtering them out
