#!/usr/bin/env python
# demonstration of data exploration code for Comp Bio course, Fall 2016
# James A. Foster
# WARNING: not completely error checked

'''
Usage:
   summarize_nonPandas.py inputFile

where inputfile is a tab delimited summary of a Hiseq dataset, as in Homework 5

Output is to stdout:

   lines beginning with # summarize when the data was created
   Others are tab delimited with a description, tab, and a summary statistic
   
Main purpose is to create data structures that I can summarize and plot later. This code is to be
reused (and adapted to Pandas).

Data structures:

for each country
   geneCount [ (gene, country ) ] = number of records for "gene" in "country"
   geneGC    [ (gene, country ) ] = gc Content of "gene" in "country"
   
Questions to answer:

- how many times does THIS gene appear in THAT country?
- what is average GC content for THIS gene in THAT country?
'''      

import sys

# print a title and the contents of the by-country dictionary, sorted, in tabular format
def showTable( title, table ):
   print( title )
   print( '\t' + '\t'.join( sorted( list( allGenes ) ) ) )
   for nextCountry in sorted( allCountries ):
      output = [ nextCountry ] 
      for nextGene in sorted( allGenes ):
         output.append( str( table.get( ( nextGene, nextCountry ), 0 ) ) )
      print( '\t'.join(output) )   

with open( sys.argv[1] ) as inFile:
   inLines = inFile.readlines()

# reformat input data into a list of tuples
allData = []
for nextLine in inLines:
   if nextLine[0] == '#': continue                 # skip comments
   tech, fwdPrimer, revPrimer, geneID, countryID, gcContent = nextLine.strip().split('\t')
   inData = ( tech, fwdPrimer, revPrimer, geneID, countryID, float(gcContent) )
   #print( "tech: %s\tfwdPrimer: %s\trevPrimer: %s\tgeneID: %s\tcountryID: %s\tgcContent: %e" % inData )
   allData.append( inData )

# gather the countries and genes, for later indexing
allCountries = { x[4] for x in allData }
allGenes = { x[3] for x in allData }

geneCount, geneGC = {}, {}

# gather data for computing gc Content (Note use of tuple as dictionary key)
for (tech, fwdPrimer, revPrimer, geneID, countryID, gcContent) in allData:
   geneCount[ ( geneID, countryID ) ] = geneCount.get( ( geneID, countryID ), 0 ) + 1
   geneGC[ ( geneID, countryID ) ] = geneGC.get( ( geneID, countryID ), 0 ) + gcContent

for (geneID, countryID) in geneGC.keys() :
   geneGC[ ( geneID, countryID ) ] = geneGC[ ( geneID, countryID ) ] / geneCount[ ( geneID, countryID ) ]

print(); showTable("gene counts by country", geneCount )
print(); showTable("gene GC content by country", geneGC )
