# Homework 1, Bash scripting, intro to Python

In this assignment gives you will learn to write a simple bash script

## To do before Thursday, 1 September (class 4)

### Readings

1. Read about markdown in git: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
2. Work through https://docs.python.org/3.5/tutorial/interpreter.html, chapters 1–3 

## To do ASAP, no later than Tuesday, 13 September (class 5)
But note that other homework are coming!
### Readings

1. Work through book, chapter 3, except pages 58—66 and 72—74
2. Work through book, appendix, pages 394—405
3. Go through grep tutorial: http://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples

### Practice Unix Commands and bash scripting
1. Create a repository on your computer to mirror the private one I invited you to. This is where you will submit homework. I recommend not putting this in your CompSkills\_F16 directory (since putting a repo in a repo can cause confusion). Something like ~/CompSkillsHomework would make sense, but this is entirely up to you. I will refer to this directory as *\<yourHomework\>*.

2. Add an appropriate README.md to this directory

3. Write a bash script named *\<yourHomework\>*/HW1/about-sequences that does the following:

	a. Outputs the text “*\<yourName\>*, summary of about-sequences”

	b. Outputs the full file information (from ls -l) about ~/CompSkills\_F16/Homework/Resources. (or whatever you called the directory in the class repo that contains stuff related to homework.)

	c. Outputs the text “Number of sequences: “

	d. Uses grep and wc to output the number of fasta records in ~/CompSkills\_F16/Homework/Resources/HW1-sequences.fsa (remember, fasta records begin with ‘>’)

	e. Outputs the last 12 lines of ~/CompSkills_F16/Homework/Resources/HW1-sequences.fsa

4. Make this script executable, and run it, redirecting the output into the file *\<yourHomework\>*/HW1/script-output.txt.

## Turn in homework

1. Commit your work

2. Update your local master

3. Sync with the remote master (that is how we will turn in homework!).

## Grading

We will grade your homework by checking script-output.txt for accuracy. 