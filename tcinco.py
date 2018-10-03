import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import matplotlib.pyplot as plt




'''
Alphabetical list of part-of-speech tags used in the Penn Treebank Project:


Tag Description

CC	Coordinating conjunction  Ex. and / with 
CD	Cardinal number one, two, three
DT	Determiner Ex. how many, how much
EX	Existential there There is an eagle. There are four flowers
FW	Foreign word Ex.tacos, pozole
IN	Preposition or subordinating conjunction Ex. or
JJ	Adjective Ex. preatty
JJR	Adjective, comparative Ex. Nancy is preattier than Alice
JJS	Adjective, superlative Ex. My friend is the best in the class
NNS	Noun, plural Ex. book / books
NNP	Proper noun, singular Ex. London
NNPS	Proper noun, plural Ex. mexican
PDT	Predeterminer
POS	Possessive ending Ex. our / us
PRP	Personal pronoun Ex. I, you, he
PRP$	Possessive pronounher
RB	Adverb Ex. easyly
RBR	Adverb, comparative Ex. more easy than
RBS	Adverb, superlative Ex. The most easy
RP	Particle Ex.
SYM	Symbol Ex: &
TO	to Ex.to eat
UH	Interjection Ex. by
VB	Verb, base form Ex. to play
VBD	Verb, past tense Ex. played
VBG	Verb, gerund or present participle Ex. playing
VBN	Verb, past participle Ex. to cr/ cried
VBP	Verb, non-3rd person singular present Ex. we stucy
VBZ	Verb, 3rd person singular present Ex. he studies
WDT	Wh-determiner Ex. some. any, more, less. few 
WP	Wh-pronoun Ex. he, she, we, they
WP$	Possessive wh-pronoun Ex. my, his. her. our. is
WRB	Wh-adverb Ex. why. where, who, 
'''






train_text=state_union.raw("2005-GWBush.txt")
sample_text="Where are you now?"


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized=custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:

		for i in tokenized:
			words=nltk.word_tokenize(i)
			tagged=nltk.pos_tag(words)

			chunkGram=r"""Chunk: {<.*>+}
						}<VB.?|IN|DT|TO>+{"""
			chunkedParser=nltk.RegexpParser(chunkGram)
			chunked= chunkedParser.parse(tagged)
			print chunked
			tagged.draw()
	except Exception as e:
		print (str(e))


process_content()
