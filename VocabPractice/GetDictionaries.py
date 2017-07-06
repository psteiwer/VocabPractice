#!/usr/bin/python
print "Content-Type: application/json"
print "Access-Control-Allow-Origin: *"
import MySQLdb,cgi
from random import randint

f=open("FrenchConnection","r")
host=f.readline()[:-1]
user=f.readline()[:-1]
pw=f.readline()[:-1]
table=f.readline()
db=MySQLdb.connect(host,user,pw,table)
cur=db.cursor()

cur.execute("SELECT distinct Source FROM Words")

counter=0
json = """
{"""
for rs in cur.fetchall():
	if counter>0:
		json=json+","
	json=json+"""
	\"Counter"""+str(counter)+"""\": \""""+str(rs[0])+"""\""""
	counter+=1 

json=json+"""
}"""

print json
