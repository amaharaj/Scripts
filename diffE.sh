#!/bin/bash

args=("$@")

file1=${args[0]}
file2=${args[1]}

if [[ $# -eq 2 ]]
then 
   paste $file1 $file2 | awk -v file1="$file1" -v file2="$file2" '{print $2-$1}' > diffE
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Takes the difference between 2 single columned files"
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: diffE.sh <file1> <file2>"
fi

