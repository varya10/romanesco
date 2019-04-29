#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Varvara Stein, mt19

import sys 
#import re, unicodedata, string
from nltk.tokenize import sent_tokenize, word_tokenize

out = sys.argv[2]
def normalize(filename):
	norm_text = ""
	with open(filename, 'r', encoding='utf-8') as infile, open(out, 'w', encoding='utf-8' ) as outfile:
		tokens = infile.read().lower()
		sents = sent_tokenize(tokens)
		for i in sents:
			norm_text = word_tokenize(i)
			outfile.write(' '.join(norm_text)+ '\n')
		
	return norm_text


def main():
	norm_text = normalize(sys.argv[1])
if __name__ == '__main__':
	main()
	