# Homework 4: using STDIN and strings
## Objectives ##

* Practice a little bash
* use I/O from STDIN
* Practice string methods
## Readings ##

### Read Before 9/22 ###
1. Read [https://docs.python.org/3.5/tutorial/modules.html](https://docs.python.org/3.5/tutorial/modules.html), section 6
2. Read about *sys.argv* in the python sys package (for example, here [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html))
### Read Before 9/27 ###
1. Read [https://docs.python.org/3.5/tutorial/inputoutput.html#reading-and-writing-files](https://docs.python.org/3.5/tutorial/inputoutput.html#reading-and-writing-files), section 7.2
2. Read [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/) about python style--this is the key information to getting a score of 3 rather than 2
## Things to do by midnight, **9/29**, or sooner
This homework will accept a series of fasta headers for sequences from STDIN, convert key information into tab-delimited format, and print the results to STDOUT. We will then redirect STDOUT to create a tab-delimited file that can be used for later analysis.

1. Create a file named *fastaHeaders.txt* with the first 10 and last 10 header records from *<Homework>/Resources/sequences.fasta*. 

>**Hint**: *grep '>' sequences.fasta | head -n 10* will get the first 10 headers. Then just redirect the output into *fastaHeaders.txt*, and do the same for the tail while being careful not to catenate overwrite your earlier results. 

>If you do this correctly, *fastaHeaders.txt* should have 20 lines. The first will be: 

>>MISEQ:7:000000000-AMAKG:1:1101:16998:1719 1:N:0:PE716:ST6_21 TTGACCCT|0|TAGACCTA|0 ST6_21_F|0|23|

>And the last will be: 

>>MISEQ:7:000000000-AMAKG:1:1101:24700:2823 1:N:0:PE724:ST6_3 TTGACCCT|0|GTACTGAC|0 ST6_3_F|1|23|

2. Write a program named *reformatReads.py* that takes a list of fasta Headers from STDIN (you will use the *sys* package for this) and, for each Header, does these things:

	a. Extracts the technology type, forward and reverse primers,  and gene name (these are the same as in the lecture notes from 9-20)

	**Hint**: In the last line, these will be *MISEQ, TTGACCCT, GTACTGAC, and ST6_3_F

	b. Extract the country of origin, which is the first two characters after the third ":" in the second field

	**Hint**: in the last line, this is *PE* (for Peru)

	c. Create a sample identifier, which should be the entire string between the third and fourth ":" in the second field, catenated with "_" and the gene name
	
	**Hint**: In the last line, this will be *PE724_ST6_3_F*

3. Print each of these fields, separated by tabs

4. Run your program and redirect the output into a file named *HW4_output.txt*

## Turn in homework
1. Commit your work to our private homework repo
2. Update your local master
3. Sync with the remote master (that is how we will turn in homework!)

Note that you are turning in **three** files:

* fastaHeaders.txt 
* reformatReads.py
* HW2_output.txt


## Grading
Grades will be as follows:

Score | Criterion
------- | ------------------------
0        | nothing turned in
1        | turned in but doesn't run or output is incorrect
2	| creates correct output
3	| does it with style (see the readings)