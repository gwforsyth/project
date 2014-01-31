#!/usr/bin/python #runs a python script

infile="GDS4467.txt"  #storing the GDS4467.txt string in the variable infile

fh = open(infile) #uses the variable infle as the argument in the open function, and stores the resulting file object in the variable fh

line = fh.readline() #reads the data on the variable fh line by line and stores the resulting string in the variable line
while line[:20] != "!dataset_table_begin": 
    line=fh.readline()

header= fh.readline().strip()#removes whitespaces

colnames={} #creating a dictionary of the columns

#Locating the location of the column
index=0
for title in header.split('\t'): 
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#open our output files, one per table.
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')

genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

def buildrow(row, fields):
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"

def build_expression(row, samples):
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
rows=0    
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))	
	rows=rows+1
    except:
	pass
genefile.close()
probefile.close()
expressionfile.close()

print '%s rows processed'%rows
    
