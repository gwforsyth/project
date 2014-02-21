#!usr/local/bin/python
import cgi
import cgitb
import os
from mod.python import apache
directory=os.path.dirname(__models.py__)
models = apache.import_module('modules', path=[directory])
cgitb.enable()

form = cgi.FieldStorage()
print "Content-Type: text/html"
print
print "<html><head><title><Project script output</title></head>"
print "<body><h1><Form Values</h1>"
form=cgi.FieldStorage()
db=models.DBhandler()
cursor=db.cursor
cursor.execute('select gene_symbol, gene_title from gene where gene_id =%s', (form['query'],))
print form['query']
print "<form method=POST action=models.py>"
print "<table><tr><td>select gene_symbol, gene_title from gene where gene_id =</td><td><input type=text name=query /></td></tr>"
print "</table>"
print "</form>"
print "</body></html>"
