# -*- coding: utf-8 -*-
import pypyodbc
import random

question=[]

def show(word):
    connection = pypyodbc.connect('Driver={SQL Server};' 
                                'Server=localhost;'
                                'Database=chat;'
                                'uid=sa;pwd=123') #conecta


    cursor=connection.cursor()
    cursor.execute("select * from "+word)#busca en la tabla
    results=cursor.fetchone()
    while results:

    	question.append(results)
        results = cursor.fetchone()
    


    connection.commit()
    select=random.randrange(0 ,len(question) ,1)
    s=""
    print ">>>",s.join(question[select])

"""
def resp(a,q):
	connection = pypyodbc.connect('Driver={SQL Server};' 
				            			'Server=localhost;'
                			    		'Database=chat;'
                            			'uid=sa;pwd=123')    			

	cursor=connection.cursor()
    cursor.execute("insert into rompe values('corre')")
    connection.commit()
    connection.close()
    	
	print "'"+a+"' ha sido agregado con la respuesta "+q
    	
"""
def main():
	ask=raw_input(">>> ")

	try:

		show(ask)
		main()


	except Exception as e:
		append=input("No se ha encontrado respuesta.\nDesea agregar una\n1.-YES\n2.-NO\n~")
		if append==1:

			del(question[0:])
			q=raw_input("Ingresa la respuesta: ")
			connection = pypyodbc.connect('Driver={SQL Server};' 
				            	'Server=localhost;'
                			    'Database=chat;'
                            	'uid=sa;pwd=123')
		

			cursor=connection.cursor()
    		cursor.execute("create table "+ask+" (respuesta varchar(50)); insert into "+ask+"values('"+q+"')")
    		connection.commit()
    		connection.close()
    		#---------------------------------------------------------------------------------
    		



		

main()