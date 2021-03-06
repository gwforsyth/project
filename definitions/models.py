from __future__ import division
'''Classes to represent our gene expression objects'''

import MySQLdb

class DBHandler(): 
	connection=None
	dbname='gwforsyth' 
	dbuser='gwforsyth'
	dbpassword='4F4Fj33A'
	
	def __init__(self): 
		'''initialisation of database'''
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
		'''retrieves the gene symbol and gene title for the gene then a list of the probe id's'''
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
		'''retrieves a list of all expression values for this gene for the specified experiment expr list = egen.get_expression('GSM12345')'''	
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

	def get_average(self,sample_id):
		'''retrieves the average gene expression value'''
		db=DBHandler()
		cursor=db.cursor()
		sql='select sum(gene_expression)/count(gene_expression)as average from gene_expression e inner join probes p on e.probe_id=p.probe_id inner join gene g on g.gene_id=p.gene_id inner join samples s on s.sample_id=e.sample_id where g.gene_id=%s and s.sample_id=%s'
		cursor.execute(sql,(self.gene_id,sample_id,))
		result=cursor.fetchone()
		print result 

class Samples():
	sample_id=''
	cell_type=''
	tissue=''

	def __init__(self,sample_id):
		'''retrieves the cell type and tissue for the gene for the specified experiment'''
		db=DBHandler()
		cursor=db.cursor()
		cellsql='select cell_type, tissue from samples where sample_id=%s'
		cursor.execute(cellsql,(sample_id,))
		result=cursor.fetchone()
		self.cell_type =result[0]
		self.tissue =result[1]

class cell():
	cell_type=''
	experiments=[]

	def __init__(self,cell_type):
		'''retrieves the sample id's for the specified cell type'''
		db=DBHandler()
		cursor=db.cursor()
		self.cell_type=cell_type
		sql='select sample_id from samples where cell_type=%s'
		cursor.execute(sql,(cell_type,))
		for result in cursor.fetchall():
			self.experiments.append(result[0])

 	def get_expression(self, sample_id):
		'''retrieves expression values for this cell type'''	
		db=DBHandler()
		cursor=db.cursor()
		sql='select gene_expression from gene_expression where sample_id=%s'
		exval=[]
		for ex in self.experiments:
			try:
				cursor.execute(sql,(ex,))	
				exval.append(cursor.fetchone()[0])
			except Exception,e:
				raise Exception('Error occured retrieving gene_expression for cell_type %s and sample_id %s:%s'%(self.cell_type,ex,e))
		return exval

	def get_average(self,sample_id):
		'''retrieves the average gene expression value'''
		db=DBHandler()
		cursor=db.cursor()
		sql='select sum(gene_expression)/count(gene_expression)as average from gene_expression e inner join probes p on e.probe_id=p.probe_id inner join gene g on g.gene_id=p.gene_id inner join samples s on s.sample_id=e.sample_id where cell_type=%s and s.sample_id=%s'
		cursor.execute(sql,(self.cell_type,sample_id,))
		result=cursor.fetchone()
		print result 
	

	def get_info(self, gene_expression):
		'''retrieves the gene and probe information for this cell type in the specified experiment'''
		db=DBHandler()		
		cursor=db.cursor()
		sql='select s.sample_id,e.gene_expression, g.gene_id, gene_title, gene_symbol, p.probe_id from gene_expression e inner join probes p on e.probe_id=p.probe_id inner join gene g on g.gene_id=p.gene_id inner join samples s on s.sample_id=e.sample_id where gene_expression=%s and s.sample_id=%s'
		gene_info=[]
		for ex in self.experiments:
			try:
				cursor.execute(sql,(gene_expression,ex,))
				result=cursor.fetchall()
				if result !='':gene_info.append(result)
			except Exception,e:
				raise Exception('Error occured retrieving the gene and probe information for sample_id %s and gene_expression %s:%s'%(ex,gene_expression,e))
		return gene_info
