import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import matplotlib.pyplot as plt
import nltk.corpus  
from nltk.text import Text  
import pypyodbc
from nltk.stem import PorterStemmer 
import random
import sys





db=[]
frase=[]



def rules(wr):


	

    connection = pypyodbc.connect('Driver={SQL Server};' 
                                'Server=localhost;'
                                'Database=piedras;'
                                'uid=sa;pwd=123') #conecta






    cursor=connection.cursor()
    cursor.execute("select * from palabras ")
    results=cursor.fetchone()
    while results:



        db.append(str(results[0]))
        results = cursor.fetchone()

        

    connection.commit()
    select=random.randrange(1 ,len(db) ,1)

    frase.append(str(db[select]))
    #print frase


def drop():
	for x in db:
		db.remove(x)
		


drop()

print "esta es la base",db
rules("PRP")
del(db[0:])
rules("NN")
del(db[0:])
rules("VBN")
del(db[0:])
rules("IN")
del(db[0:])
rules("DT")
del(db[0:])
rules("JJ")
s=" "
print s.join(frase)
del(frase[0:])
del(db[0:])
		
print "esta es la base",db 