# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 00:49:29 2023

@author: ABDOULAHI FAYE
"""
# =============================================================================

# TD sur le langage SQLite
# EXO1
import sqlite3
conn = sqlite3.connect('school.db') 
cur = conn.cursor() 
# Insérer une ligne de données 
cur.execute("""create table if not exists students( 
            name text,
            e_mail text,
            phone integer,
            section text)""")
nom=input('saisir le votre nom:')
email=input('saire votre email:')
numero=input('saisir le numero:')
section= input('votre section')
cur.execute(""" insert into students(name,e_mail,phone,section) values (?,?,?,?),(nom,
            'email,numero,'section')""")
#oikl,cur.execute("""select* from students""")
#print(cur.fetchall())
# =============================================================================
# Engager l'opération 
#cur.execute("""delete from students""")
conn.commit() 
# Fermer la connexion 
conn.close()
