import sys
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

data_fpath = r'data/sample.txt'
corpus_fpath = r'data/corpora.txt'

nltk.data.load(corpus_fpath,format='raw')

corpus = PlaintextCorpusReader(corpus_fpath,".*",encoding='latin1')

print(corpus)

with open(data_fpath,"r") as f:
	for ln in f:
		token = nltk.word_tokenize(ln)
		pos = nltk.pos_tag(token)

		nouns = [wd[0] for wd in pos if wd[1]=="NN" or wd[1]=="NNS"]

		print(nouns)