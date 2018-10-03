#C:\Users\Alejandro Bec\AppData\Roaming\nltk_data\corpora\gutenberg
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import matplotlib.pyplot as plt
import nltk.corpus  
from nltk.text import Text  




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





"""
train_text=state_union.raw("2005-GWBush.txt")
sample_text="Where are you now?"


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized=custom_sent_tokenizer.tokenize(sample_text)"""
textList = Text(nltk.corpus.gutenberg.words('texto.txt'))

def process_content():
	try:

		for i in textList:
			words=nltk.word_tokenize(i)
			tagged=nltk.pos_tag(words)


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

			print chunkedwrb
			chunkedwrb.draw()
		textList.plot()
		#print sorted(set(textList)) 
		print len(set(textList))
			


	except Exception as e:
		print (str(e))


process_content()
