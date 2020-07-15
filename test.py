import nltk
import unicodedata
from nltk.corpus import stopwords
from fractions import Fraction

# function to handle fractions
def fraction(word):

	try:
		return str(unicodedata.numeric(word))
	except Exception as e:
		return word



if __name__=="__main__":

	data_fpath = r'data/lumpia_mollica.txt'
	corpus_fpath = r'data/corpora.txt'

	with open(corpus_fpath,"r") as stop:

		cook_stop = [wd.strip('\n') for wd in stop.readlines()]


	with open(data_fpath,"r") as rcp:
		for ln in rcp.readlines()[1:]: # skip first line
			token = nltk.word_tokenize(ln)

			# sweep for fractions
			frc_sweep = [fraction(wd) for wd in token]

			filtered = [wd for wd in frc_sweep if wd not in cook_stop]

			pos = nltk.pos_tag(filtered)

			print(pos)

			nouns = [wd[0] for wd in pos if wd[1]=="NN" or wd[1]=="NNS"]
			
			# TODO: handle different kinds of milk (sweetened condensed, evaporated)
			# by splitting ingredients parsing into 2 stages
			# 1st stage: detailed preprocessed ingredients (Nouns + adverbs)
			# 2nd stage: raw ingredients (chicken, milk)
