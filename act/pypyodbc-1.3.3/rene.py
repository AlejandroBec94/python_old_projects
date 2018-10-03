#C:\Users\Alejandro Bec\AppData\Roaming\nltk_data\corpora\gutenberg
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import matplotlib.pyplot as plt
import nltk.corpus  
from nltk.text import Text  
import psycopg2, psycopg2.extras
from nltk.stem import PorterStemmer 
import random
import sys
import tkinter
from tkinter import *
import ttk
import sys


db=[]


top = tkinter.Tk()
# Code to add widgets will go here...

top.geometry("500x250")


listbox = tkinter.Listbox(top,width=50, height=10)

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


def show(conpal):

	conn=psycopg2.connect(database='piedras',user='postgres',password=64689499,host='localhost')
	cur=conn.cursor()

	cur.execute("select * from "+conpal)

	for row in cur :
		db.append(row)    

   # connection.commit()

#---------------------------------------------------------------

frase=[]
def rules(wr):


	

    conn=psycopg2.connect(database='piedras',user='postgres',password=64689499,host='localhost')
    cur=conn.cursor()
    cur.execute("select (palabra) from palabras where tipo like'%"+wr+"))'")
   
    for row in cur:


        db.append(row[0])
        

        

    
    select=random.randrange(1 ,len(db) ,1)

    frase.append(str(db[select]))
    #print frase
    


#----------------------------------------------------------------
textList = Text(nltk.corpus.gutenberg.words('texto.txt'))

def process_content():

	conn=psycopg2.connect(database='piedras',user='postgres',password=64689499,host='localhost')


	list=[]
	show("palabras")

	try:

		for i in textList:

			print "\n\n"

			words=nltk.word_tokenize(i)
			tagged=nltk.pos_tag(words)

			ps=PorterStemmer()
			

			
                


			CC=r"""Coordinating conjunction   : {<CC.?>} """
			CD=r"""Cardinal number   : {<CD.?>} """
			DT=r"""Determiner   : {<DT.?>} """
			EX=r"""Existential   : {<EX.?>} """
			FW=r"""Foreign word   : {<FW.?>} """
			IN=r"""Preposition or subordinating conjunction   : {<IN.?>} """
			JJ=r"""Adjective   : {<JJ.?>} """
			JJR=r"""Adjective, comparative   : {<JJR.?>} """
			JJS=r"""Adjective, superlative   : {<JJS.?>} """
			NN=r"""Noun  : {<NN.?>} """
			NNS=r"""Noun, plural   : {<NNS.?>} """
			NNP=r"""Proper noun, singular   : {<NNP.?>} """
			NNPS=r"""Proper noun, plural   : {<NNPS.?>} """
			PDT=r"""Predeterminer   : {<PDT.?>} """
			POS=r"""Possessive ending   : {<POS.?>} """
			PRP=r"""Personal pronoun   : {<PRP.?>} """
			RB=r"""Adverb   : {<RB.?>} """
			RBR=r"""Adverb, comparative   : {<RBR.?>} """
			RBS=r"""Adverb, superlative   : {<RBS.?>} """
			RP=r"""Particle   : {<RP.?>} """
			SYM=r"""Symbol   : {<SYM.?>} """
			TO=r"""To   : {<TO.?>} """
			UH=r"""Interjection   : {<UH.?>} """
			VB=r"""Verb, base form   : {<VB.?>} """
			VBD=r"""Verb, past tense   : {<VBD.?>} """
			VBG=r"""Verb, gerund or present participle   : {<VBG.?>} """
			VBN=r"""Verb, past participle   : {<VBN.?>} """
			VBP=r"""Verb, non-3rd person singular present   : {<VBP.?>} """
			VBZ=r"""Verb, 3rd person singular present   : {<VBZ.?>} """
			WDT=r"""Wh-determiner   : {<WDT.?>} """
			WP=r"""Wh-pronoun   : {<WP.?>} """
			WRB=r"""Wh-adverb   : {<WRB.?>} """
			#WPs	=r"""Possessive wh-pronoun    : {<WP$.?>}"""
		

			cc=nltk.RegexpParser(CC)
			cd=nltk.RegexpParser(CD)
			dt=nltk.RegexpParser(DT)
			ex=nltk.RegexpParser(EX)
			fw=nltk.RegexpParser(FW)
			inn=nltk.RegexpParser(IN)
			jj=nltk.RegexpParser(JJ)
			jjr=nltk.RegexpParser(JJR)
			jjs=nltk.RegexpParser(JJS)
			nn=nltk.RegexpParser(NN)
			nns=nltk.RegexpParser(NNS)
			nnp=nltk.RegexpParser(NNP)
			nnps=nltk.RegexpParser(NNPS)
			pdt=nltk.RegexpParser(PDT)
			pos=nltk.RegexpParser(POS)
			prp=nltk.RegexpParser(PRP)
			rb=nltk.RegexpParser(RB)
			rbr=nltk.RegexpParser(RBR)
			rbs=nltk.RegexpParser(RBS)
			rp=nltk.RegexpParser(RP)
			sym=nltk.RegexpParser(SYM)
			to=nltk.RegexpParser(TO)
			uh=nltk.RegexpParser(UH)
			vb=nltk.RegexpParser(VB)
			vbd=nltk.RegexpParser(VBD)
			vbg=nltk.RegexpParser(VBG)
			vbn=nltk.RegexpParser(VBN)
			vbp=nltk.RegexpParser(VBP)
			vbz=nltk.RegexpParser(VBZ)
			wdt=nltk.RegexpParser(WDT)
			wp=nltk.RegexpParser(WP)
			wrb=nltk.RegexpParser(WRB)
			#wps=nltk.RegexpParser(WPs)

			chunkedcc=cc.parse(tagged)
			chunkedcd=cd.parse(chunkedcc)
			chunkeddt=dt.parse(chunkedcd)
			chunkedex=ex.parse(chunkeddt)
			chunkedfw=fw.parse(chunkedex)
			chunkedin=inn.parse(chunkedfw)
			chunkedjj=jj.parse(chunkedin)
			chunkedjjr=jjr.parse(chunkedjj)
			chunkedjjs=jjs.parse(chunkedjjr)
			chunkednn=nn.parse(chunkedjjs)
			chunkednns=nns.parse(chunkednn)
			chunkednnp=nnp.parse(chunkednns)
			chunkednnps=nnps.parse(chunkednnp)
			chunkedpdt=pdt.parse(chunkednnps)
			chunkedpos=pos.parse(chunkedpdt)
			chunkedprp=prp.parse(chunkedpos)
			chunkedrb=rb.parse(chunkedprp)
			chunkedrbr=rbr.parse(chunkedrb)
			chunkedrbs=rbs.parse(chunkedrbr)
			chunkedrp=rp.parse(chunkedrbs)
			chunkedsym=sym.parse(chunkedrp)
			chunkedto=to.parse(chunkedsym)
			chunkeduh=uh.parse(chunkedto)
			chunkedvb=vb.parse(chunkeduh)
			chunkedvbd=vbd.parse(chunkedvb)
			chunkedvbg=vbg.parse(chunkedvbd)
			chunkedvbn=vbn.parse(chunkedvbg)
			chunkedvbp=vbp.parse(chunkedvbn)
			chunkedvbz=vbz.parse(chunkedvbp)
			chunkedwdt=wdt.parse(chunkedvbz)
			chunkedwp=wp.parse(chunkedwdt)
			chunkedwrb=wrb.parse(chunkedwp)
			#chunkedwps=wps.parse(chunkedwrb)

			print chunkedwrb


			if ps.stem(i) in db:

				print "La palabra '", i,"' ha sido registrada con anterioridad."
				listbox.insert(1,"La palabra '%s' ha sido registrada con anterioridad."%i)
				

			else:

				if not(i.isalpha()): 
                
					print "Palabra %s no valida."%ps.stem(i)
					#listbox.insert(1,ps.stem(i))
					listbox.insert(1,"Palabra '%s' no valida."%ps.stem(i))

				else:


					cur=conn.cursor()
					cur.execute("insert into palabras values (\'%s',\'%s')"% (i,chunkedwrb))
					conn.commit()
					print "Palabra '",i,"' registrada"
					listbox.insert(1,"Palabra '%s' registrada"%i)
					
					db.append(i)

	
			"""
		textList.plot()
		"""
		#print sorted(set(textList)) 
		
		


	except Exception as e:
		print (str(e))

def drop():
	for x in db:
		db.remove(x)
		

def main():
	print ("\n0.-Escanear texto\n1.-Mostrar Grafica de palabras\n2.-Mostrar numero de palabras sin repetir\n3.-Crear Frases\n4.-Mostrar etiquetas\n5.-Salir ")
	opc=input("\nElige una opcion: ")

	if opc==0:
		process_content()
		main()

	elif opc==1:

	 	plt.title("Palabras")
		textList.plot()
		main()
		


	elif opc==2:
		print "\n\nNumero de palabras sin repetir: ",len(set(textList))
		main()

	elif opc==3:
		del(db[0:])
		#print "esta es la base",db
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
		del(db[0:])
		s=" "
		print "\n",s.join(frase)
		del(frase[0:])
		
		#print "esta es la base",db
		main()


	elif opc==4:
		print """ Alphabetical list of part-of-speech tags used in the Penn Treebank Project:



Tag Description

CC	Coordinating conjunction  Ex. and / but
CD	Cardinal number one, two, three
DT	Determiner Ex. how many, how much
EX	Existential there There is an eagle. There are four flowers
FW	Foreign word Ex.tacos, pozole
IN	Preposition or subordinating conjunction Ex. in on under
JJ	Adjective Ex. pretty intelligent
JJR	Adjective, comparative Ex. Nancy is prettier than Alice
JJS	Adjective, superlative Ex. My friend is the best in the class
NNS	Noun, plural Ex. book / books man men
NNP	Proper noun, singular Ex. London
NNPS	Proper noun, plural Ex. mexican
PDT	Predeterminer Ex. once, twice, all, nether 
POS	Possessive ending Ex. our / us
PRP	Personal pronoun Ex. I, you, he
PRP$	Possessive pronoun Ex. her, my, their
RB	Adverb Ex. easyly
RBR	Adverb, comparative Ex. more easy than
RBS	Adverb, superlative Ex. The easiest
RP	Particle Ex.made
SYM	Symbol Ex: &
TO	to Ex.to eat
UH	Interjection Ex. by then as long as
VB	Verb, base form Ex. to play
VBD	Verb, past tense Ex. played
VBG	Verb, gerund or present participle Ex. playing
VBN	Verb, past participle Ex. to cr/ cried
VBP	Verb, non-3rd person singular present Ex. he studies
VBZ	Verb, 3rd person singular present Ex. he studies
WDT	Wh-determiner Ex. some. any, more, less. few 
WP	Wh-pronoun Ex. he, she, we, they
WP$	Possessive wh-pronoun Ex. my, his. her. our. is
WRB	Wh-adverb Ex. why. where, who, """
		main()

	elif opc==5:
		sys.exit(0)
	else:
		print "Elige una opcion de la lista."
		main()


boton = tkinter.Button(top, text="Procesar.", command=process_content)


w = tkinter.Label(top, text="Numero de palabras sin repetir: "+str(len(set(textList))))		
w.pack()
listbox.pack()
boton.pack()
top.title("Proyecto Final Piedras")
bit = top.iconbitmap('p.ico')
center(top)
top.mainloop()

