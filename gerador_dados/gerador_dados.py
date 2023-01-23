# -*- coding: utf-8 -*- 

import time
import psycopg2
import pandas as pd
from datetime import datetime

def conecta_db():
	con = psycopg2.connect(host='localhost', database='db',user='admin', password='admin')
	return con

def criar_db(sql):
	con = conecta_db()
	cur = con.cursor()
	cur.execute(sql)
	con.commit()
	con.close()

def inserir_db(sql):
	con = conecta_db()
	cur = con.cursor()
	try:
		cur.execute(sql)
		con.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error: %s" % error)
		con.rollback()
		cur.close()
		return 1
	finally:
		cur.close()

def consultar_db(sql):
	con = conecta_db()
	cur = con.cursor()
	cur.execute(sql)

	recset = cur.fetchall()
	registros = []
	for rec in recset:
		registros.append(rec)
	con.close()
	return registros

def consulta_db(sql):
	con = conecta_db()
	cur = con.cursor()
	cur.execute(sql)
	recset = cur.fetchall()
	for rec in recset:
		print (rec)

if __name__ == '__main__':
	df = pd.read_csv('data.csv', sep=';')

	for i in df.head(10).index:
		sql = """INSERT into sensores (time, temp, umid, press) values ('{}',{},{},{});""".format(datetime.now(), df['TEMPERATURA DO AR - BULBO SECO, HORARIA'][i].replace(',','.'), df['UMIDADE RELATIVA DO AR, HORARIA'][i], df['PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA'][i].replace(',','.'))
		inserir_db(sql)
		time.sleep(15)
		print(sql)