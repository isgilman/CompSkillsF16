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
   allDataFrame = pd.read_table( sys.argv[1], comment='#', usecols=[ 'Gene','Country','gcContent' ] )
except OSError as err:
   print( "**ERROR** Cannot open %s, error: %s" % ( sys.argv[1], err ) )
except:
   print( "**ERROR** unknown error with %s: %s" % ( sys.argv[1], sys.exc_info()[0] ) )

allDataFrame['GeneFamily'] = [x[:x.find('_')] for x in allDataFrame['Gene'] ]
allDataFrame['highGC'] = allDataFrame.gcContent > 0.4
allDataFrame['lowGC']  = allDataFrame.gcContent < 0.4

print( allDataFrame.describe(include='all') )

# summarize GC content by country
gcByCountry = DataFrame( index={x for x in allDataFrame.Country}, 
                        columns=['mean','std'] )
for nextCountry in sorted( gcByCountry.index ): # sorted( set( allDataFrame.Country ) ):
   #same as: nextMean, nextSTD = allDataFrame[ allDataFrame.Country == nextCountry ].describe().ix[['mean','std'],'gcContent'] 
   thisRow = allDataFrame[ allDataFrame.Country == nextCountry ]
   theseStats = thisRow.describe()
   nextMean, nextSTD = theseStats.ix[['mean','std'],'gcContent']
   gcByCountry.ix[ nextCountry ] = [nextMean, nextSTD ]

# summarize GC content by gene family
gcByGeneFamily = DataFrame( index={x for x in allDataFrame.GeneFamily}, 
                        columns=['mean','std'] )
for nextGF in sorted( gcByGeneFamily.index ):
   theseStats = allDataFrame[ allDataFrame.GeneFamily == nextGF ].describe()
   nextMean, nextSTD = theseStats.ix[['mean','std'],'gcContent']
   gcByGeneFamily.ix[ nextGF ] = [ nextMean, nextSTD ]

print( gcByCountry )
print( gcByGeneFamily )
