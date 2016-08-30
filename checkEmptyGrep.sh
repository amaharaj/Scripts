#!/bin/bash

path_to_file=$2
var=$1

if [[ $# -eq 2 ]]
then 
   line=$(grep "$var" $path_to_file)
   if [ $? -eq 1 ]
       then
       echo "EMPTY OUTPUT"
       echo $path_to_file
       exit 1
   fi
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "   Checks to see if output of grep is empty   "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: checkEmptyGrep.sh <variable to grep for> <working-dir/filename>"
fi
