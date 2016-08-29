#!/bin/bash

args=("$@")

path_to_file=${args[0]}

if [[ $# -eq 1 ]]
then 
   if [ -e $path_to_file ];then
      echo "Found file"
      pwd
      echo $path_to_file
   else
      echo "Did not find file"
      pwd
      echo $path_to_file
   fi
else 
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Checks to see if file exists in specified path "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: checkExist <working-dir/filename>"
fi
