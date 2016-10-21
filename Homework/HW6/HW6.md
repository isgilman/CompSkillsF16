# Homework 6: Human microbiome analysis
We will begin analysis of an actual dataset from a human vaginal microbiome study. 

In this assignment we will read in an actual empirical datasets,  and do some simple data processing. 

This dataset is a human microbiome dataset. Vaginal swabs from 25 women were taken daily for 10 weeks by the Forney (UI) and Ravel (UMD) labs. Each sample was analyzed for microbial content using 16S amplicon analysis and high performance sequencing. The numbers in columns below bacterial species names are the number of sequences in that row that could be ascribed to that species, using Bayesian analysis. I have pruned the full dataset to only include a few high-abundance species, and only the first four days of the first and last week of sampling.

These data are from Ravel, J., Brotman, R. M., Gajer, P., Ma, B., Nandy, M., Fadrosh, D. W., et al. (2013). Daily temporal dynamics of vaginal microbiota before, during and after episodes of bacterial vaginosis. Microbiome, 1(1), 29. [DOI 10.1186/2049-2618-1-29](http://doi.org/10.1186/2049-2618-1-29). The full dataset is available as described in the paper.

## Objectives ##
* Process more realistic data (with some errors!)
## Readings, by 10/20 
1. Read and meditate upon *The Zen of Python*, [https://en.wikipedia.org/wiki/Zen_of_Python](https://en.wikipedia.org/wiki/Zen_of_Python)
2. Read [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
2. Work through [https://docs.python.org/3.5/tutorial/errors.html](https://docs.python.org/3.5/tutorial/errors.html)
3. Work through textbook, Chapter 5, *Getting Started with Pandas*, pages 107--132
## Things to do before midnight, **10/27**, or sooner
Write a program named *microbiome.py* that does the following (please do **not** use pandas, we will do that later):

1. Read *../Resources/vaginal_communities.txt* into an appropriate data structure. 

	Later you will want to group the data by patientID and timepoint (which is derived from week and day), and you will display data for each microbial group. 

	a. In your comments, justify your choice of this data structure, so the next programmer knows **why** you did it this way.

2. Change all OTU counts to relative abundances (the relative abundance is the read counts--the number in columns--divided by the total count in *Total*)

	OTUs are Operational Taxonomic Units, groups of similar sequences which are named by looking up those sequences in an existing database. Sometimes this is a species name, sometimes it is not.

	a. Be sure to handle errors (there are likely to be some, since this is real-world data)
3. Compute the average relative abundance of each OTU for each patient (averaged over all time points).

	a. Be sure to handle errors (there are likely to be some, since this is real-world data)
	
4. Write a tab delimited file named *avgRelativeAbundances.txt* that has the patient ID and the average relative abundances for each OTU.

	a. Sort the records by the patient ID

	b. Keep the columns in the same relative order as in the input file

	c. Retain the column headers from the input file. (we will use this file in later assignments)
## Turn in homework

1. Commit your work
2. Update your local master
3. Sync with the remote master

## Grading
Grades will be determined as follows:

Grade | Criteria 
-------- | --------------
0          | Nothing turned in
1          | Code turned in but doesn't run, or is incorrect
2          | *avgRelativeAbundances.txt* is correct
3          | *avgRelativeAbundances.txt* is correct, and code uses good style (as per our readings on style)