#!usr/local/bin/python
import cgi
import cgitb
cgitb.enable()
import models.py

form=cgi.FieldStorage()
print "Content-Type: text/html"
print
print "<html><head><TITLE><CGI script output</TITLE></head>"
print "<body><H1><Form Values</H1>"
print"<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
	print "<tr><td>%s</th><th>%s</td></tr>"%(k,form[k])
print "<table>"
print"</body></html>"
add query stuff here



