# Homework 3
In this assignment you will revise your program from Homework 2 to use function definitions and iterations through lists and strings.

## Readings ##

####Before class on 9/15 (Thursday)
1. Read Book pages 416 to 419 (functions), 406 to 407 (slicing)
2. Work through [https://docs.python.org/3.5/tutorial/](https://docs.python.org/3.5/tutorial/) section 5.1 to 5.3

###Before class on 9/20
1. Read Book pages 409 to 416 (dicts, sets, comprehension)
2. Work through [https://docs.python.org/3.5/tutorial/](https://docs.python.org/3.5/tutorial/) section 5.4 to 5.8

## Coding to do by **midnight, 9/22, or sooner**
Revise your program from homework 2 as follows:

1. Define a function named *CountNucs* that takes two argument, a string *s* and a character *c* and returns the number of times *c* occurs in *s* (yes, this does the same thing as *s.count(c)*)
2. Create a int list of length 7, named *Counts* 
3. Use *CountNucs* to count the number of A's, C's, G's, T's, N's, Y's, and U's
4. Set *Counts[i]* to the number of times the *i*th nucleotide in *['A','C','G','T','N','Y','U']* occurs in each sequence (for example, *Counts[1]* should be the number of 'C's in the sequence, which is 15 for the first sequence)
4. for each sequence (see below), print to *stdout* (one per line)
 
>"Sequence: *s*", where *s* is the sequence you are working on

>"*n* occurs *i* times", for each nucleotide *n*, where *i* is the number of times *n* occurs in the sequence

>"The sequence has *n* nucleotides, where *a* (*p* percent) are ambiguous", where *n* is the length of your string, *a* is the number of ambiguity codes, and *p* is $a/n$

>a blank line (to separate output for each of the two input sequences)


Run your program on the following two sequences (these are the same as in Homework 2), redirecting the output to a file named *nucleotide_counts.txt* in the same directory as your program:

>CGCAGCTAACGCATTAAGCACTCCGCCTGGGGAGTACGACCGCAAGGTTGAA
	CGGATCGTAAAGCTCTGTTGTTGGTGAAGAAGGATAGAGGTAGTAACTGGCCT


###Notes 
1. in a DNA sequence, N, Y, and U are "ambiguity codes". N means the nucleotide could not be determined, Y means the nucleotide is a pyrimidine, U means the nucleotide is a purine. There are other ambiguity codes
2. *print* can take multiple arguments, and will print them one after another. For example, *print( c,'occurs', n, 'times' )* will print something like what you want in step (4)

### Questions to Ponder ###
1. How can you design your program so that you can add a new ambiguity code, changing only one line in the code?
2. which is faster, your code or the *str.count()* method? 

## Turn in homework
1. Commit your work to a separate homework 3 directory in your private repo (the one for us to grade). Note that you should have two files, the program and the output.
2. Update your local master
3. Sync with the remote master (that is how we will turn in homework!)

## Grading
We will grade your homework as follows: 0 if you don't do it, 1 if you do it but it doesn't work, 2 if you do it and it works, 3 if it works and you follow the style guidelines in section 4.8 of the online tutorial [https://docs.python.org/3.5/tutorial/controlflow.html#intermezzo-coding-style](https://docs.python.org/3.5/tutorial/controlflow.html#intermezzo-coding-style)