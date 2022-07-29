import sqlite3

conn = sqlite3.connect('aal_polta_fs_listing_DB.sqlite')
print ("Opened database successfully")

conn.execute('''CREATE TABLE DRIVE_DETAILS
    (FILENAME        TEXT    ,
    FULLPATH          TEXT   ,
    FILESIZE          TEXT   ,
    LAST_MOD_DT          TEXT   ,
    FILEEXT         TEXT);''')


conn.commit() 

print ("Table created successfully")

conn.close()
