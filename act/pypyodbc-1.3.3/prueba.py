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




textList = Text(nltk.corpus.gutenberg.words('texto.txt'))

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


	print i
