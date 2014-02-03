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
		gene_symbol=''
		gene_title=''
		gene_id=''
		probelist=[]

	def __init__(self,geneid):
		self.gene_id=geneid
		db=DBHandler()
		cursor=db.cursor() #link to database
		sql='select gene_title, gene_symbol from gene where gene_id =%s' #pull out data about gene
		cursor.execute(sql,(geneid,))
		#query database
		#get result and populate the class fields
		result=cursor.fetchone()
		self.gene_title =result[0]
		self.gene_symbol =result[1]
		#now fetch the  probes..
		probesql='select probeid from probe where geneid=%s'
		#fill in the blanks

		for result in cursor fetchall():
			self.probelist.append(result[0])
	
	def get_expression(self): #by variables from sample description, experiment

	
