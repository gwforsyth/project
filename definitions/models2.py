'''Classes to represent our gene expression objects'''

import MySQLdb

class DBHandler(): #database handler class
	connection=None
	dbname='mydatabase' #class level variables
	dbuser='gwforsyth'
	dbpassword='4F4Fj33A'
	
	
def __init__(self): #initialisation
		if DBHandler.connection == None: #test to see if connection has been defined
			DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

def cursor(self):
	return DBHandler.connection.cursor() #make database run each time

class Samples():
	sample_id=''
	cell_type=''
	tissue=''
	
def __init__(self, sample_id):
	self.sample_id=sample_id
	db=DBHandler()
	cursor=db.cursor() #link to database
	sql='select cell_type, tissue from samples where sample_id =%s'
	cursor.execute(sql,(sample_id))
	result=cursor.fetchone()
	self.cell_type=result[0]
	self.tissue=result[1]
	for r in result:
		print "%s"%(r[0])
		
	

