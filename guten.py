
#C:\Users\Alejandro Bec\AppData\Roaming\nltk_data\corpora\gutenberg
import nltk.corpus  
from nltk.text import Text  
#number=input("Numero de Palabras:   ")

list=[]
textList = Text(nltk.corpus.gutenberg.words('cuento.txt'))
for x in textList:
	#word=raw_input("Palabra:   ")
	list.append(x)


	#textList.concordance(word)
textList.dispersion_plot(list)
#textList.plot()
print len(set(textList))
