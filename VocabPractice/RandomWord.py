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

frenchword=''
englishword=''
hiddenword=''
displayword=''

confidence=randint(1,100)
if confidence<=85:
    confidence=1
elif confidence>95:
    confidence=3
else:
    confidence=2


while ((frenchword=='') and (englishword=='')):
    cur.execute("SELECT French,English,Confidence FROM Words WHERE Confidence=%s ORDER BY RAND() LIMIT 1",confidence)

    for rs in cur.fetchall():
        frenchword=rs[0]
        englishword=rs[1]
        confidence=rs[2]

json = """
{
    \"frenchword\": \""""+str(frenchword)+"""\",
    \"englishword\": \""""+str(englishword)+"""\",
    \"confidence\": \""""+str(confidence)+"""\"
}"""

print json
