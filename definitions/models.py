'''Classes to represent our gene expression objects'''

import MySQLdb

class DBHandler(): #database handler class
	connection=None
	dbname='gwforsyth' #class level variables
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
		
	probelist=[] #each gene has many probes
	
	def __init__(self,gene_id):
		db=DBHandler()
		self.gene_id=gene_id
		cursor=db.cursor()
		sql='select gene_symbol, gene_title from gene where gene_id =%s' #pull out data about gene
		cursor.execute(sql,(gene_id,))
		#query database
		#get result and populate the class fields
		result=cursor.fetchone()
		self.gene_symbol =result[0]
		self.gene_title =result[1]
		
		#now fetch the  probes..
		probesql='select probe_id from probes where gene_id=%s'
		cursor.execute(probesql,(gene_id,))
		#resultlist=cursor.fetchall()

		for result in cursor.fetchall():
			self.probelist.append(result[0])
	
	def get_expression(self,sample_id):
		'''retrieves a list of all expression values for this gene for the specified experiment
expr list = egen.get_expression('GSM12345')
'''	
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_expression from gene_expression where probe_id=%s and sample_id=%s'
		exvals=[]
		for p in self.probelist:
			try:
				cursor.execute(sql,(p,sample_id,))	
				exvals.append(cursor.fetchone()[0])
			except Exception,e:
				raise Exception('Error occured retrieving gene_expression data for probe_id %s and sample_id %s:%s'%(p,sample_id,e))
		return exvals
 
