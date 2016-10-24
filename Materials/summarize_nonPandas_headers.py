#!/usr/bin/env python
# demonstration of data exploration code for Comp Bio course, Fall 2016
# James A. Foster
# WARNING: not completely error checked

'''
Usage:
   summarize_nonPandasHeaders.py inputFile

where inputfile is a tab delimited summary of a Hiseq dataset, as in Homework 5 but WITH HEADERS

**Main point** is to show how headers are usually handled

Output is to stdout:

   lines beginning with # summarize when the data was created
   Others are tab delimited with a description, tab, and a summary statistic
   
Main purpose is to create data structures that I can summarize and plot later. This code is to be
reused (and adapted to Pandas).

Data structures:

for each country
   geneCount [ (gene, country ) ] = number of records for "gene" in "country"
   geneGC    [ (gene, country ) ] = gc Content of "gene" in "country"

'''      

import sys

# print a title and the contents of the by-country dictionary, sorted, in tabular format
def showTable( title, table ):
   print( title )
   allGenes = sorted( { g for (g,c) in geneCount } )        # set comprehension
   allCountries = sorted( { c for (g,c) in geneCount } )    # set comprehension
   print( '\t' + '\t'.join( allGenes ) )
   for nextCountry in sorted( allCountries ):
      output = [ nextCountry ] 
      for nextGene in sorted( allGenes ):
         output.append( str( table.get( ( nextGene, nextCountry ), 0 ) ) )
      print( '\t'.join(output) )   

with open( sys.argv[1] ) as inFile:
   inLines = inFile.readlines()

allData, seenHeader = [], False
geneCount, geneGC = {}, {}

for nextLine in inLines:
   if nextLine[0] == '#': continue                 # skip comments
   if seenHeader:
      inData = nextLine.strip().split('\t')
      inData[-1] = float( inData[-1] )
      inDataDict = dict( zip( Headers, inData ) )  # the header trick
      geneID, countryID = inDataDict[ 'Gene' ], inDataDict[ 'Country' ]
      
      geneCount[ ( geneID, countryID ) ] = geneCount.get( ( geneID, countryID ), 0 ) + 1
      geneGC[ ( geneID, countryID ) ] = geneGC.get( ( geneID, countryID ), 0 ) + inDataDict[ 'gcContent' ]
   else:
      Headers = nextLine.strip().split('\t')       # get the headers
      seenHeader = True

# convert GC content counts into ratios
for (geneID, countryID) in geneGC :
   geneGC[ ( geneID, countryID ) ] = geneGC[ ( geneID, countryID ) ] / geneCount[ ( geneID, countryID ) ]

print(); showTable("gene counts by country", geneCount )
print(); showTable("gene GC content by country", geneGC )
