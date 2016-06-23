#!/bin/bash

args=("$@")

if [[ $# -eq 1 ]]
then
   awk '{if (NR==1) printf "%5.8f \n", $1}' ${args[0]} > firstE
   shiftE=$(<firstE)

   if [[ $(echo "$shiftE<0" | bc) == 1 ]]; then
      awk '{printf "%5.8f \n", sqrt($1^2)}' firstE > abs_E
      shiftE=$(<abs_E)
      awk -v shiftE="$shiftE" '{printf "%5.8f \n", $1+shiftE}' ${args[0]} > shifted_energy 
   else
      awk -v shiftE="$shiftE" '{printf "%5.8f \n", $1-shiftE}' ${args[0]} > shifted_energy
   fi
   rm abs_E firstE
fi 
if [[ $# -ne 1 ]]
then
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Shifts data by the first entry"
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: fistEShift.sh <file>"
fi

