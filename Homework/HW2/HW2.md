latex input:	mmd-article-header  
latex input:	ftp-metadata 
Title:	Homework 2, first python
Date:	2016-09-08 
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

# Homework 2: a simple python program
Here, you will write a simple python program. Note that this one can be ugly if necessary, but it has to be correct. We will modify this in later homework.

Please put all your work in a directory named HW2 on your private repo, so we can keep the different homework solutions separated.
## Readings ##
Remember: in your readings it will help to try out the things you read about on a computer; and to keep track of confusing or unclear terms, examples, and errors you discover so we can discuss them in class.
###For class on 9/13
1. Work through https://docs.python.org/3.5/tutorial/interpreter.html, chapters 4.1-4.5, 4.8
2. Work through book, appendix, pages 381--394, review 394—405
3. Read book introduction to Chapter 4, pages 75-76. If you want to, skim the rest of chapter 4. This is useful stuff, but really hard to digest at this point.
###For class on 9/15
1. Work through https://docs.python.org/3.5/tutorial/interpreter.html, chapters 4.6-4.7
### Review ####
Remember, you can look at the markdown code for these homework assignments as examples of markdown formatting.
## Things to do by midnight, Thursday, 9/15, or sooner
Create a file named *count_nucleotides.py* that does the following

1. Counts the number of A's, C's, G's, and T's in the following two DNA sequences (note that the first has 53 nucleotides and the second 54)

	a.  CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA

	b.  CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT
    
2. Prints the following output

		sequence: *sequence*
		A's: *number of A's*
		C's: *number of C's*
		T's: *number of T's*
		G's: *number of G's*
		GC content: *gc content*
   
	Where *number of x's* is the number of nucleotide *x* in *sequence* and *gc content* is the gc content of *sequence* is $\frac{\mbox{(number of G's)} + \mbox{(number of C's)}}{\mbox{length of sequence}}$

For example, with sequence "AAGGCCC" the output should be (the gc content may have more or fewer significant digits on your system)

		sequence: *sequence*
		A's: 2
		C's: 3
		T's: 0
		G's: 2
		GC content: 0.714285714

Run your program and redirect the output into a file (in the same directory) named *ncounts.txt*
## Turn in homework
1. Commit your work
2. Update your local master
3. Sync with the remote master

## Grading
We will grade your homework by the accuracy of the contents of *ncounts.txt*. For this assignment, we will grade on a three point scale: 0 if you don't do it, 1 if you do it but the output is incorrect, 3 if the output is correct. 
## Objectives of This Assignment ##
1. Write and run a simple python program using strings, ints, floats, loops, print(), and arithmetic
