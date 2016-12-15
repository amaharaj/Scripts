#!/bin/bash 

args=("$@")

mkdir xsf-cv

path_to_xsf=${args[0]}

if [[ $# -eq 3 ]]
then 
   file1=${args[1]}
   file2=${args[2]}
   list_exclude=$(cat $file1 $file2)
   echo "$list_exclude"
 
elif [[ $# -eq 2 ]]
then 
   list_exclude=${args[1]} 
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "  Separate cross-validation data and store in xsf-cv     "
   echo "  folder. Provide list of train data, test data or both  "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: genCVdata.sh <path-to-all-xsf-files> <Train Data> Optional: <Test Data>"
fi

rsync -avz --exclude-from <( echo $list_exclude) $path_to_xsf xsf-cv/


