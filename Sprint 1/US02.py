# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 12:52:45 2017

@author: rishi
"""

import sqlite3
import datetime
conn=sqlite3.connect('GEDCOM_DATA.db')
conn.text_factory = str

query1="select NAME,BIRTHDAY,MARRIED from INDIVIDUAL AS I,FAMILY AS F where I.ID=F.HUSBAND_ID OR I.ID=F.WIFE_ID"  

result1=conn.execute(query1)

value=result1.fetchall()
first=value[0]
#print(first[1])

#a=datetime.datetime.strptime(first[1],'%d %b %Y')
#print a.strftime('%d %m %Y')

i=0
for row in value:
    first_row=value[i]
    a=datetime.datetime.strptime(first_row[1],'%d %b %Y')
    a.strftime('%d %m %Y')
    
    b=datetime.datetime.strptime(first_row[2],'%d %b %Y')
    a.strftime('%d %m %Y')
    i+=1
  #  print (first_row)
    if(a > b):
        print (first_row[0],"is born after their own marriage which is not possible ")
   
 #   else:
  #      print (first_row[0],"is born before marriage")
    