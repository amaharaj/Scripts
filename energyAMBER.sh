#!/bin/bash

# run as ./energyAMBER.sh <infile> 

args=("$@")


if [[ $# -eq 1 ]]
then

   awk '/ENERGY/ {getline; print $0}' ${args[0]} > Total_Energy
fi
if [[ $# -ne 1 ]]
then
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Get energy from AMBER output file"
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: energyAMBER.sh <file>"
fi

