
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import nltk, os, sys 
print "\n\n CONCORDANCES SEARCH ENGINE \n" 

print "These are the files in your current directory \n" 

print os.listdir('.') 
print "\n\n Insert the text filename you want to work with\n" 
thefile=raw_input() 

f=open(thefile, 'rU') 
text=f.read() 
textD=text.split() 

textDS=nltk.Text(textD) 

print "\n Introduce the word you want to find \n" 

theword=raw_input() 

print "\n Concordances with \"" + theword + "\"\n" 
results=textDS.concordance(theword) 
print "\n" 
print results 

outfile = "concordance_with_"+theword+".txt" 
final = open(outfile, "w") 

#### HERE IS WHERE IT DOES NOT WORK 
final.write(results) 
#### 

final.close() 
print "Succesfuly saved \n" 