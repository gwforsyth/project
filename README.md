#21.01.14 
Created a new repository called project.
Found a dataset on GEO with the title Primary and Seconday brain tumours: giloblastomas, astrocytomas and oligodendrogliomas.  The dataset contains 35 samples. 

#23.01.14
Finally created a table! In the dataset the 
first 37 columns contained data I wasn't interested in.
However all original attempts at loading the dataset 
into the table weren't successful.  I wanted to insert
columns 38-41 into my table but columns 1-3 inserted instead. 
Original command: LOAD DATA LOCAL INFILE 'GDS4467' INTO TABLE data5 
IGNORE 1 LINES (gene_title, gene_symbol, gene_id);
Working command: LOAD DATA LOCAL INFILE 'GDS4467' INTO TABLE data5 
IGNORE 1 LINES 
(@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, 
@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, 
@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, 
@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, 
@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, 
@dummy, @dummy, @dummy, @dummy, @dummy, @dummy, 
@dummy, gene_title, gene_symbol, gene_id);

I am sure there is an easier way to do this, but for
now it will do!

#30.01.14
So over the last few days a lot has happened. In my definitions repository I
now have files including  my GEO data, a python script to preprocess the data 
and a file containg processed data for the samples table. The python script 
is "the easier way to insert the data into my table".  Still got a few tweaks to 
make to it.  For the samples table the data was modified in a text editor,
since its content didn't come from the GEO table but the GEO script. 
I don't really know how I did it, but I made a mistake at somepoint whilst 
trying to upload data to git.  I managed to have copies of all my files in 
my project rep and my definitions rep.  The other thing I managed to do was 
create another definitions rep within the original definitions rep. I believe
these issue may have had something to do with me adding everything whilst in
the wrong directory... maybe?? Seem to have got everything tidied up now and 
will need to be more careful with adding things in future.

#31.01.14 
yesterday I forgot to upload the files which were produced from the python script which preprocessed the dataset data.

#03.02.14
Just uploaded a script which contains the commands to create python classes.  This script was based on a script which Dr Martin had written to which I changed to fit my data. 
There is only one class in the script so far; the gene class

#04.02.14
Since I have a virtual machine set up on my laptop I can work on my project at home. To save recreating all the tables in MySQL again, a file was created which contained all the necessary information using the command mysqldump

#11.02.14 
Have now added a samples and a cell class to the models script. Within the samples and gene class the expression values are found and the average calculated.

#14.02.14
Have started to write a webpage script to where users will be able to query the models script.

#18.02.14
The webpage now a an query box which links to the cgi script but an error is returned.  Will leave it at that so project report can be written

