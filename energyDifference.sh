#!/bin/bash

# run as ./energyDifference.sh <file> <outfile>
# <file> must be a single column of numerical values

args=("$@")

if [[ $# -eq 2 ]]
then
   awk 'NR>1{printf "%5.8f \n", $1-p } {p=$1}' ${args[0]} > ${args[1]}
fi
if [[ $# -ne 2 ]]
then
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Get the difference in energy between steps"
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: energyDifference.sh <file>"
fi

