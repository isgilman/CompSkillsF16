#!/usr/bin/env python
# demonstration of data exploration code for Comp Bio course, Fall 2016
# James A. Foster
# WARNING: not completely error checked

'''
Usage:
   summarize_Pandas.py inputFile

where inputfile is a tab delimited summary of a Hiseq dataset, as in Homework 5

Questions to answer:

- how many times does THIS gene appear in THAT country?
- what is average GC content for THIS gene in THAT country?
'''      

import sys
import pandas as pd
from pandas import Series, DataFrame

# read data from input file
try:
   with open( sys.argv[1] ) as inFile:
      inLines = inFile.readlines()
except OSError as err:
   print( "**ERROR** Cannot open %s, error: %s" % ( sys.argv[1], err ) )
except:
   print( "**ERROR** unknown error with %s: %s" % ( sys.argv[1], sys.exc_info()[0] ) )

# In this program we read the input into a list and then convert to a Pandas array. 
# it would be cleaner to just use the Pandas file I/O capabilities from the start
allData = []
for nextLine in inLines:
   if nextLine[0] == '#': continue
   tech, fwdPrimer, revPrimer, geneID, countryID, gcContent = nextLine.strip().split('\t')
   inData = ( tech, fwdPrimer, revPrimer, geneID, countryID, float(gcContent) )
   #print( "tech: %s\tfwdPrimer: %s\trevPrimer: %s\tgeneID: %s\tcountryID: %s\tgcContent: %e" % \
   #   inData )
   allData.append( inData )

# Create the Pandas DataFrame from the input data list
allDataFrame = DataFrame( allData, 
   columns=['Tech', 'fwdPrimer', 'revPrimer', 'Gene', 'Country', 'gcContent', ] 
   )
