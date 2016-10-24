latex input:	mmd-article-header  
latex input:	ftp-metadata 
Title:	HW7, processing microbiome data
Date:	2016-10-24
Base Header Level:	2  
latex mode:	article  
Keywords:	MultiMarkdown, Markdown, XML, XHTML, XSLT, PDF   
copyright:	2016 James A. Foster  
	This work is licensed under a Creative Commons License.  
	http:	//creativecommons.org/licenses/by-nc-sa/3.0/  
htmlheader:	<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>
latex input:	mmd-natbib-plain
latex input:	mmd-article-begin-doc  
latex footer:	mmd-article-footer  

# Homework 7: Human microbiome analysis, part II

We will continue analysis of two actual 
datasets from a human vaginal microbiome study. 

In this assignment we will read in two actual empirical datasets, combine the data, and do some simple data processing. 

This dataset is a metadata dataset from a human microbiome project. In addition to microbiome data in the previous assignment, the 25 women kept a daily diary of health and sexual practice related information. I have pruned the full dataset to only include a few metadata items, and only the first four days of the first and last week of sampling. It is very common in human microbiome studies to combine microbial community data with patient metadata, as we are doing here. 

Ravel, J., Brotman, R. M., Gajer, P., Ma, B., Nandy, M., Fadrosh, D. W., et al. (2013). Daily temporal dynamics of vaginal microbiota before, during and after episodes of bacterial vaginosis. Microbiome, 1(1), 29. [DOI 10.1186/2049-2618-1-29](http://doi.org/10.1186/2049-2618-1-29). The full dataset is available as described in the paper.

## Objectives ##
* Process more realistic data (with some errors!)
* Create summary files
## Readings, by 10/27
1. Work through textbook, Chapter 5, *Getting Started with Pandas*, pages 133--143
## Things to Do Before Midnight, **11/3**, or Sooner ##
Write a program named *microbiome_summary.py* that uses pandas to do the following:

1.  Read *../Resources/vaginal_communities.txt* into a pandas dataframe named *summaryByDay*

	a. Change all OTU counts to relative abundances (the relative abundance is the read counts--the number in columns--divided by the total count in *Total*)

	b. Drop the following columns (or just don't add them): 'ID', 'time', 'Week', 'Day', 'Batch_ID', 'Date'. **NOTE** you will keep the column 'sampleID' and 'patientID'
	
3. In a different dataframe, called *summaryByWeek*, compute the average relative abundance of *each OTU for each patient for weeks 1 and 10* (that is, each patient will have two rows). This dataframe will lack columns: 'ID', 'time', 'Week', 'Day', 'Batch_ID', 'Date'. **NOTE** you will keep the column 'sampleID' and 'patientID'.

	a. Be sure to update the Totals column to be the total reads for each of the two weeks 

	c. Add a column with the *Shannon Diversity Index* for each row

	The *Shannon Diversity Index* is $\sum_{1,N} \frac{r_i}{\log r_i}$ where $N$ is the number of OTU columns, $\log$ is the natural logarithm, and $r_i$ is the relative abundance of the OTU $i$. This is a common measure of species diversity in an ecosystem (though technically we should be using probabilities, rather than relative abundances--but let that slide.) Note that the log function is in the *numpy* package and is named *log* (so you will want an *import numpy as np* and *np.log()* somewhere in your code.)

	d. Add another column with the *Inverse Simpson Diversity Index* for each row.

	The *Inverse Simpson Diversity Index* is $\left( \sum_{1,N} r_i^2 \right)^{-1}$ where $N$ and $r_i$ are as above.

4. In a different dataframe, called *summaryByWoman*, compute the average relative abundance of *each OTU for each patient* (that is, there will be one row per patient, summarizing the data for that patient). This dataframe will also lack columns: 'ID', 'time', 'Week', 'Day', 'Batch_ID', 'Date'. **NOTE** you will keep the column 'sampleID' and 'patientID'

		a. Be sure to update the Totals column 
		b. Add a column with the *Shannon Diversity Index* for each row
		c. Add another column with the *Inverse Simpson Diversity Index* for each row
	
4. Write these dataframes as tab delimited files with the same names: *summaryByDay.txt*, *summaryByWeek.txt*, and *summaryByWoman.txt*. You will use this for the next two assignments.You will use this in the next assignment.

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

## Hints ##
* Notice that this is essentially doing the same things three times. That is a good opportunity for using function definitions. 
* You might want to use the full datasets (all 10 weeks, all 25 days) someday. So, it's a good idea to not hard-code weeks 1 and 10.
* Ask yourself how the actual data in the files can screw up your computations (division by zero, wrong datatype) and how to handle those cases. 