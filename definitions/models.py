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

	class Gene(): #define class gene
		gene_id=''
		gene_symbol=''
		gene_title=''
		
		probelist=[] #find out what this means
	
	def __init__(self,gene_id):
		self.gene_id=gene_id
		db=DBHandler()
		cursor=db.cursor() #link to database
		sql='select gene_symbol, gene_title from gene where gene_id =%s' #pull out data about gene
		cursor.execute(sql,(gene_id))
		#query database
		#get result and populate the class fields
		result=cursor.fetchone()
		self.gene_symbol =result[0]
		self.gene_title =result[1]
		
		#now fetch the  probes..
		probesql='select probe_id from probe where gene_id=%s'
		cursor.execute(probesql,(geneid))
		result=cursor.fetchone()
		self.probe_id =result[2]

		for result in cursor.fetchall():
			self.probelist.append(result[0])
	
	#def get_expression(self)
class Probe():
		probe_id=''
		gene_id=''	
	
	class Samples(): 
		sample_id=''
		cell_type=''
		tissue=''

	class Gene_expression():
