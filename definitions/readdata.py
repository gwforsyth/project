#!/usr/bin/python #runs a python script

infile="GDS4467.txt"  #storing the GDS4467.txt string in the variable infile

fh = open(infile) #uses the variable infle as the argument in the open function, and stores the resulting file object in the variable fh

line = fh.readline() #reads the data on the variable fh line by line and stores the resulting string in the variable line
while line[:20] != "!dataset_table_begin": 
    line=fh.readline()

header= fh.readline().strip()#defines the header as the lines without blank spaces

colnames={} #creating a dictionary of the columns

#Locating the location of the column
index=0
for title in header.split('\t'): 
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1


#open our output files for writing, one per table.
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')
#assigning the correct fields that corresond to the columns in the tables
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

def buildrow(row, fields):
    '''creating new rows for the datafields'''
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"

def build_expression(row, samples):
    '''adds the data from the datasets into the text files'''
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
#closing the files
genefile.close()
probefile.close()
expressionfile.close()

#printing a messaage of rows processed
print '%s rows processed'%rows
    
