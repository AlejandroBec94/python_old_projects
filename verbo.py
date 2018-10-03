#-*- coding:utf-8 -*-
import nltk
from nltk.corpus import treebank



my_file=open("este_mero.py","r")
cont=my_file.read()
        #
    #return cont
my_file.close() 

sentence=cont
tokens=nltk.word_tokenize(sentence)
print (tokens,"\n")

tagged=nltk.pos_tag(tokens)
entities=nltk.chunk.ne_chunk(tagged)
print (entities)