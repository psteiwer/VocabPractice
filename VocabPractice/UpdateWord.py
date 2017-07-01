#!/usr/bin/python
print "Content-Type: text/html\n\n"
import MySQLdb,cgi

f=open("FrenchConnection","r")
host=f.readline()[:-1]
user=f.readline()[:-1]
pw=f.readline()[:-1]
table=f.readline()
db=MySQLdb.connect(host,user,pw,table)
cur=db.cursor()

form=cgi.FieldStorage()
frenchword=form.getvalue('FrenchWord')
confidence=form.getvalue('Confidence')
englishword=form.getvalue('EnglishWord')
sql=""

if confidence!=None:
    print "Confidence: %s" % confidence
    print "FrenchWord: %s" % frenchword
    sql="UPDATE Words SET Confidence=%d WHERE French='%s'" % (int(confidence),str(frenchword).replace("'","''"))
    cur.execute(sql)
    db.commit()
    
elif englishword!=None:
    print "FrenchWord: %s" % frenchword
    print "EnglishWord: %s" % englishword
    sql="INSERT into Words (French,English,Confidence) VALUES ('%s','%s',1)" % (frenchword,englishword)
    cur.execute(sql)
    db.commit()

cur.close()
db.close()
print sql
