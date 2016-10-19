#!/usr/bin/env python
# demonstration of data exploration code for Comp Bio course, Fall 2016
# James A. Foster
# WARNING: not completely error checked

'''
Usage:
   summarize_Pandas.py inputFile

where inputfile is a tab delimited summary of a Hiseq dataset, as in Homework 5

Output is to stdout:

   lines beginning with # summarize when the data was created
   Others are tab delimited with a description, tab, and a summary statistic

Questions to answer:

- how many times does THIS gene appear in THAT country?
- what is average GC content for THIS gene in THAT country?
'''      

import sys
import pandas as pd
from pandas import Series, DataFrame

# Print summary information in tabular format
def showTable( title, table ):
   print( title )
   print( '\t' + '\t'.join( sorted( list( allGenes ) ) ) )
   for nextCountry in sorted( allCountries ):
      output = [ nextCountry ] 
      for nextGene in sorted( allGenes ):
         output.append( str( table.get( ( nextGene, nextCountry ), 0 ) ) )
      print( '\t'.join(output) )   

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

allCountries = { x[4] for x in allData }
allGenes = { x[3] for x in allData }

# Create the Pandas DataFrame from the input data list
allDataFrame = DataFrame( allData, 
   columns=['Tech', 'fwdPrimer', 'revPrimer', 'Gene', 'Country', 'gcContent', ] 
   )

# accessing columns
allDataFrame[ 'Country' ]
allDataFrame.Country

# accessing rows
allDataFrame.ix[1]      # using an index

# manipulating columns
allDataFrame['GeneFamily'] = None

allDataFrame['highGC'] = allDataFrame.gcContent > 0.5
allDataFrame['lowGC']  = allDataFrame.gcContent < 0.3

# other stuff
allDataFrame.values
allDataFrame.index

# re-order and drop columns
headers=['gcContent','highGC', 'lowGC', 'Gene', 'Country', 'fwdPrimer', 'revPrimer', ]
allDataFrame.reindex(columns=headers)
allDataFrame.drop(['fwdPrimer', 'revPrimer', ], axis=1)

highGC = allDataFrame[ allDataFrame['gcContent'] > 0.4 ]

# .ix for cutting both vertically and horizontally
allDataFrame.ix[ allDataFrame.gcContent>0.4, [ 'Gene' ] ]

'''
# from old program
geneCount, geneGC = {}, {}

for (tech, fwdPrimer, revPrimer, geneID, countryID, gcContent) in allData:
   geneCount[ ( geneID, countryID ) ] = geneCount.get( ( geneID, countryID ), 0 ) + 1
   geneGC[ ( geneID, countryID ) ] = geneGC.get( ( geneID, countryID ), 0 ) + gcContent

for (geneID, countryID) in geneGC.keys() :
   geneGC[ ( geneID, countryID ) ] = geneGC[ ( geneID, countryID ) ] / geneCount[ ( geneID, countryID ) ]

print(); showTable("gene counts by country", geneCount )
print(); showTable("gene GC content by country", geneGC )
'''