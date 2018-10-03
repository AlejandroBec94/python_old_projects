# -*- coding: utf-8 -*-
import psycopg2, psycopg2.extras
import random
import re
import sys

question=[]

def show(word):
    del(question[0:])
    conn=psycopg2.connect(database='piedras',user='postgres',password=64689499,host='localhost')
    cur=conn.cursor()
    cur.execute("select * from "+word)#busca en la tabla
    
    for row in cur:
        question.append(row[0])
        
        select=random.randrange(0 ,len(question) ,1)
    print question[select]


def otro(a):

    q = raw_input("Ingresa la respuesta:\n>>> ")
    conn=psycopg2.connect(database='piedras',user='postgres',password=64689499,host='localhost')
    cur=conn.cursor()
    cur.execute("create table "+a+" (palabra varchar(50));insert into "+a+" values (\'"+q+"\')")
    conn.commit()
    main()
        

def main():
    try:
        ask = raw_input(">>> ")

        try:
            
            c=ask.split()
            s="_"
            c=s.join(c)
            cadena = re.sub("\W", "", c)

            show(cadena)
            main()

        except Exception as ex:
            run = input("No se ha encontrado respuesta para esto.\nDesea agregar una respuesta?\n1.-Si\n2.-No\n>>> ")

            c=ask.split()
            s="_"
            c=s.join(c)
            cadena = re.sub("\W", "", c)
            if run == 1:
                otro(cadena)

            elif run == 2:
                
                main()
    except Exception as e:
        print"EROR!!!  "*6
     


main()

