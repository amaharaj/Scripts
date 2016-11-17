#!/bin/bash

args=("$@")

infile=${args[0]}
outfile=${args[1]}

if [[ $# -eq 2 ]]
then
   # generate H-H pair correlation curve
   echo " $infile
   $outfile-H-H
   H
   H
   4.0
   0.01
   0
   14.41, 14.41, 14.41" | ~/git/RDF/RDF

   # generate H-O pair correlation curve
   echo " $infile
   $outfile-H-O
   H
   O
   4.0
   0.01
   0
   14.41, 14.41, 14.41" | ~/git/RDF/RDF

   # generate O-O pair correlation curve
   echo " $infile
   $outfile-O-O
   O
   O
   4.0
   0.01
   0
   14.41, 14.41, 14.41" | ~/git/RDF/RDF
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "      Automatically passes arguments to RDF script,      "
   echo "  curves for H-H, O-H and O-O are generated in one pass  "
   echo "  NOTE: outfile will be appended with H-H, O-H or O-O.   "
   echo "        (3 files will be produced)                       "
   echo "  NOTE: must edit RDF_stats.sh script to change box size,"
   echo "        bin size, and xrange                             "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: RDF_stats.sh <infile> <outfile>"
fi

