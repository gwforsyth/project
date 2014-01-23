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
