# Homework 5: parsing and processing fasta files
## Objectives:

* use 
	* file I/O
	* dictionaries
* Practice/review
	* shebang, chmod
	* *Sys* module, argv[]
	* practice re-using code
### Readings (by 10/6 or sooner)
1. Review dictionaries [https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries](https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries)
2. Review loops and function definitions [https://docs.python.org/3.5/tutorial/controlflow.html](https://docs.python.org/3.5/tutorial/controlflow.html)
3. Work through [https://docs.python.org/3.5/tutorial/errors.html#](https://docs.python.org/3.5/tutorial/errors.html#)

## Things to do before midnight, **10/13**, or sooner (**was 10/6**)
###Write code to parse fasta file, keep selected data items
Write *parseHiseq.py* to do the following (**note** this is a modification of the solution to HW4)

1. Work as a standalone executable (that is, add the appropriate shebang and set the appropriate modifications) 
2. Use the first parameter passed at runtime as the name of a fasta file which is the output of an Illumina HISEQ run
3. Use the second parameter passed at runtime as the name of an output file

	Example: For 2 and 3, if you run your program with the command 
>*./parseHiseq.py ../Resources/sequences.fasta myOutput.tsv*

	where *sequences.fasta* is an appropriate file, then your program will read from *sequences.fasta* and write the output to *myOutput.tsv*
	
4. For each fasta Header (lines beginning with '>', read from the file that you identified in step 2), extract the *technology type*, *forward* and *reverse primers*, *gene name*, and *country of origin*. Create a *sample identifier*, which should be the entire string between the third and fourth “:” in the second field, catenated with “_” and the gene name. 

	*Note:* you did this in HW4, feel free to reuse your code.

	a. Create a list comprising technology type, forward primer, reverse primer, gene name, and country of origin 
	
	b. Add this list to a dictionary named *sequenceData*, using the sample identifier as a key
	
5. For each DNA sequence, 

	a. Add the sequence (in upper case) to a dictionary named *sequences*, using the sample identifier from 4a as the key
	
	b. Compute the GC content for this sequence (ignoring ambiguity codes)
	
	c. Append the GC content to the end of the appropriate entry in the *sequenceData* dictionary

At this point, *parseHiseq.py* will have code to extract a bunch of information, including data directly from the headers, data derived from the headers, and the DNA sequences, and to add these data to two separate dictionaries.
### Write Code to Calculate and Report Important Data ###

Add code to *parseHiseq.py* to:

1. Write the following to the output file identified as the second parameter at runtime:

		# Input file *inputFileName*
		# Output file *outputFileName*
		# Sequences processed: *numberOfSequences*
		# Average sequence length: *averageLength*
		# Average GC Content: *averageGC*

Where

		*inputFileName* is the input file name (first runtime parameter)
		*outputFileName* is the output file name (second runtime parameter)
		*numberOfSequences* is the number of DNA sequences processed (note, should be the number of lines that begin with '>' in the input file)
		*averageLength* is the average number of nucleotides per DNA sequence
		*averageGC* is the average GC content of the DNA sequences

>**Note** that in order to output these values, you will have to compute them.

2. For each DNA sequence, write the following data fields, in this order, separated by tabs: 
>*technology type*, *forward* and *reverse primers*, *gene name*, and *country of origin*, and *GC Content*

### Run Your Program ###
In your private repository (the one we grade), run your program using *../Resources/sequences.fasta* as input and *seqDataOutput.txt* as output.
	
## Turn in homework
1. Commit your work
2. Update your local master branch in your private (graded) repo
3. Sync with the remote master (to turn in homework!).
## Grading
Grades will be determined as follows:

Grade | Criteria 
-------- | --------------
0          | Nothing turned in
1          | Code turned in but doesn't run, or is incorrect
2          | *seqDataOutput.txt* is correct
3          | *seqDataOutput.txt* is correct, and code uses appropriate function definitions

## Hints ##

* There are several steps to this program, so get small chunks working correctly first. 

>For example, you can work on chunks such as these independently: get run time arguments, open/read input file, open and write to output file, parse headers, create dictionary with parsed data, add code to read sequences, create dictionary for sequences, compute and write lines beginning with '#', add code to write tab delimited data

* Create a **smaller** file (4 lines is probably enough!) to use while you are working on your code, work out the correct output by hand. Be sure the test file is correctly formed (one header in the right format for each DNA sequence)
* We **will** be modifying this code in later homework assignments--so be kind to yourself with comments, variable names, and good modular code!