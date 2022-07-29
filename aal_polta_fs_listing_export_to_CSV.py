import sqlite3
import csv
import codecs 

encoding="utf-8"
encoder = codecs.getincrementalencoder(encoding)()

def encodeone(item):
   if type(item) == unicode:
      return  encoder.encode(item)
   else:
      return item


try:
   conn = sqlite3.connect("aal_polta_fs_listing_DB.sqlite")
   csvWriter = csv.writer(open("aal_polta_fs_listing_driveFileSurvey.csv", "w"))
   conn.text_factory = str
   cur  = conn.cursor()
   rows = cur.execute("SELECT * FROM DRIVE_DETAILS")
   #rows = c.fetchall()
   for row in rows:
      csvWriter.writerow(encodeone(row))

except Exception as e : 
   print ( str (e) ) 
   pass 
