latex input:	mmd-article-header  
latex input:	ftp-metadata 
Title:	HW7, processing microbiome data
Date:	2016-10-27
Base Header Level:	2  
latex mode:	article  
Keywords:	MultiMarkdown, Markdown, XML, XHTML, XSLT, PDF   
copyright:	2016 James A. Foster  
	This work is licensed under a Creative Commons License.  
	http:	//creativecommons.org/licenses/by-nc-sa/3.0/  
htmlheader:	<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
latex input:	mmd-natbib-plain
latex input:	mmd-article-begin-doc  
latex footer:	mmd-article-footer  

# Homework 7: Human microbiome analysis, part II ***DRAFT***

We will continue analysis of two actual 
datasets from a human vaginal microbiome study. 

In this assignment we will read in two actual empirical datasets, combine the data, and do some simple data processing. 

This dataset is a metadata dataset from a human microbiome project. In addition to microbiome data in the previous assignment, the 25 women kept a daily diary of health and sexual practice related information. I have pruned the full dataset to only include a few metadata items, and only the first four days of the first and last week of sampling. It is very common in human microbiome studies to combine microbial community data with patient metadata, as we are doing here. 

## Objectives ##
* Process more realistic data (with some errors!)
* Combine two datasets
* Create a summary file
## Readings, by 10/27
1. Work through textbook, Chapter 5, *Getting Started with Pandas*, pages ???--???
## Things to Do Before Midnight, **10/20**, or Sooner ##
Write a program named *microbiome_summary.py* that uses pandas to do the following:
#### Compute Diversity Metrics ####
1.  Read *../Resources/vaginal_communities.txt* into a pandas dataframe 
2. Change all OTU counts to relative abundances (the relative abundance is the read counts--the number in columns--divided by the total count in *Total*)
3. In a different dataframe, compute the average relative abundance of each OTU for each patient for weeks 1 and 10 (that is, each patient will have two rows).

	a. Drop the following columns (or just don't add them): ID, time, sampleID, Day, Batch_ID, Date

	b. Be sure to update the Totals column to be the total reads for each of the two weeks 

	c. Add a column with the *Shannon Diversity Index* for each row

	The *Shannon Diversity Index* is $\sum_{1,N} \frac{r_i}{\log r_i$ where $N$ is the number of OTU columns, $\log$ is the natural logarithm, and $r_i$ is the relative abundance of the $i$th OTU. This is a common measure of species diversity in an ecosystem (though technically we should be using probabilities, rather than relative abundances--but let that slide.) Note that the log function is in the *numpy* package and is named *log* (so you will want an *import numpy as np* and *np.log()* somewhere in your code.)

	d. Add another column with the *Inverse Simpson Diversity Index* for each row.

	The *Inverse Simpson Diversity Index* is $\left( \sum_{1,N} r_i^2 \right)^{-1}$ where $N$ and $r_i$ are as above.
4. Write a tab delimited file named *diversity_summary.txt* that has all the columns from above (that is, other than *ID, time, sampleID, Day, Batch_ID, and Date*, including the diversity metrics). You will use this in the next assignment.
#### Add Metadata ####
Later, we will look for correlations between microbiome changes and patient metadata.

1. Read *../Resources/vaginal_metadata.txt* into a pandas dataframe 
2. Drop the first three columns (*ID, DATE_COM, and SITE2*)
3. Merge the **first** dataframe from above (the one with a row for each day) with this one, using the patient name as the common field.

	Beware, there may be some rows that don't match up. Again, this is real data, and that sort of thing happens all the time.

4. Add the Shannon and Inverse Simpson indexes for each sample (note: if you aren't using functions, you're doing too much work)

5. Write this (combined) dataframe as a tab delimited file named *cooked_data.txt*. You will use this for the next two assignments.

## Turn in homework
As usual:

1. Commit yor work
2. Update your local master
3. Sync with the remote master

## Grading
Grades will be determined as follows:

Grade | Criteria 
-------- | --------------
0          | Nothing turned in
1          | Code turned in but doesn't run, or is incorrect
2          | *diversity_summary.txt* and *cooked_data.txt* are correct
3          |  *diversity_summary.txt* and *cooked_data.txt* are correct, and code uses good style (as per our readings on style)