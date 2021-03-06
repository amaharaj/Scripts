#!/bin/bash

args=("$@")

if [[ $# -eq 1 ]]
then

   awk '{ sum += $1 } END { if (NR > 0) printf "%5.8f \n", sum / NR }' ${args[0]} > average

   mean=$(<average)

   if [[ $(echo "$mean<0" | bc) == 1 ]]; then
      awk '{printf "%5.8f \n", sqrt($1^2)}' average > abs_average
      mean=$(<abs_average)
      awk -v mean="$mean" '{printf "%5.8f \n", $1+mean}' ${args[0]} > shifted_energy 
   else
      awk -v mean="$mean" '{printf "%5.8f \n", $1-mean}' ${args[0]} > shifted_energy
   fi

   rm abs_average average
fi

if [[ $# -ne 1 ]]
then
    echo " "
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"    
    echo "Shifts data of a single column input file by the average of the column"
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo " " 
    echo "Usage: averageShift.sh <single column file>"
fi


