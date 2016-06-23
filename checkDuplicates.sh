#!/bin/bash

args=("$@")

if [[ $# -eq 1 ]]
then
   sort ${args[0]} | uniq -d | grep -nFxf - ${args[0]}
fi 
if [[ $# -ne 1 ]]
then 
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Checks for duplicate lines in a file"
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: checkDuplicates.sh <file>"
fi 
