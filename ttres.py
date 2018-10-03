from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()
example=["I","Working","in","Mexico","because","i","dont","have","money."]


for w in example:
	print (ps.stem(w))

"""
new_text="Its very important to be pythonly while you are pythoning with python.All pythoners have pythoned poorly at least once."

words=word_tokenize(new_text)
for w in words:
	print (ps.stem(w))
"""