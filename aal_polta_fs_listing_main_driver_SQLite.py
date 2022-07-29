
import os, sys
import datetime 
import sqlite3

#radius_driveFIleCount_vFSz.py
#gTargetDriveStr = 'C:\\Users\\mlashkar\\U_Drive_Backup\\PY_HOME\\radius_projects\\storage_survey'
#gTargetDriveStr = '/home/sas/HOME_PY'

gTargetDriveStr = '~/palashworld/_dev/HOME_PY/syncDir'
db_loc_1 = 'aal_polta_fs_listing_DB.sqlite'

def isLinux():
	print("In IsLinux")
    if sys.platform == 'win32':print("win32")
    if os.environ.get('OS','') == 'Windows_NT':print("winNT")
    if os.name == 'nt':print("nt")

class FILE_DETAILS_CLS:
    def __init__ (self):
        self.filename= None # or whatever
        self.fullpath = None 
        self.size_in_KB = None
        self.last_mod_dt = None
        self.extn = None
        
    def printContent(self): 
        print ( '\n filename =' , self.filename, '\n fullpath =' , self.fullpath,'\n size_in_KB =' , self.size_in_KB, '\n  self.last_mod_dt =' ,  self.last_mod_dt , '\n Extension =' , self.extn)


def listToPathString ( pList) :   
    return ''.join((str(e)+'\\') for e in pList)



def loadInto_DRIVE_DETAILS_DB ( pTableDataStrct ): 
    conn = sqlite3.connect(db_loc_1)  
    cur = conn.cursor() 

    sql_query = "insert into DRIVE_DETAILS (FILENAME, FULLPATH, FILESIZE, LAST_MOD_DT, FILEEXT ) values (?, ?, ?, ?, ?)"   
    sql_data = (pTableDataStrct.filename,  pTableDataStrct.fullpath,  pTableDataStrct.size_in_KB, pTableDataStrct.last_mod_dt, pTableDataStrct.extn)

    try:
        cur.execute(sql_query, sql_data)
        conn.commit()

    except sqlite3.Error as er:
        print ( 'Error = ', er)
        #self.output_exc()

    cur.close()  
    
    
    
    
def countDriveFiles ( pDrivePathStr):  
	
    print ("Surveying path : " + pDrivePathStr + " , for file attributes....." )  
    dir_count = 0
    file_count = 0  
    fullPath = '' 
    
    isLinux()
    
    for root, dirs, files in os.walk(pDrivePathStr):
        file_deatils_obj = FILE_DETAILS_CLS()
        
        dir_count += len(dirs)
        file_count += len(files)     
        
        path = root.split(os.sep)
        lev1 = listToPathString(path)
        for file in files:
            fullPath = os.path.join(root, file)
           
            file_deatils_obj.filename = file 
            file_deatils_obj.fullpath = (lev1 + file).replace(' ','') 
            file_deatils_obj.extn = os.path.splitext(file_deatils_obj.fullpath)[1]
            file_deatils_obj.size_in_KB  =  format (os.stat(fullPath).st_size, '.2f')
            file_deatils_obj.last_mod_dt =  datetime.datetime.fromtimestamp(os.stat(fullPath).st_mtime)
            
            file_deatils_obj.printContent() 
           
            loadInto_DRIVE_DETAILS_DB ( file_deatils_obj)
            
    print ("\nDrive path survey co " , pDrivePathStr)           
    print ("\nDir_count = ", dir_count )
    print ("\nFile_count = ", file_count )
    


countDriveFiles (gTargetDriveStr)



#print time.ctime(max(os.stat(root).st_mtime for root,_,_ in os.walk('/tmp/x'))):
