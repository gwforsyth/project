#21.01.14 
Created a new repository called project.
Found a dataset on GEO with the title Primary and Seconday brain tumours: giloblastomas, astrocytomas and oligodendrogliomas.  The dataset contains 35 samples. 

#23.01.14
Finally created a table! In the dataset the 
first 37 columns contained data I wasn't interested in.
However all original attempts at loading the dataset 
into the table weren't successful.  I wanted to insert
columns 38-41 into my table but columns 1-3 inserted instead. 

#Original command: 
LOAD DATA LOCAL INFILE 'GDS4467' INTO TABLE data5 
IGNORE 1 LINES (gene_title, gene_symbol, gene_id);

#Working command: 
LOAD DATA LOCAL INFILE 'GDS4467' INTO TABLE data5 
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
