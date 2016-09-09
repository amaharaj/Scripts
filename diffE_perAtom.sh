#!/bin/bash

args=("$@")

file1=${args[0]}
file2=${args[1]}

if [[ $# -eq 2 ]]
then 
   paste $file1 $file2 | awk -v file1="$file1" -v file2="$file2" '{print (($2-$1)*1000.0)/(300.0)}' > diffE
   #abs=$(<diffE)
   awk '{printf "%5.8f \n", sqrt($1^2)}' diffE > MAE
  # if [[ $(echo "$abs<0" | bc ) ==1 ]]; then 
   #   awk -v abs="$abs" '{printf "%5.8f \n", $1+shiftE}' ${args[0]} > shifted_energy
   #else
   #   awk -v abs="$abs" '{printf "%5.8f \n", $1-shiftE}' ${args[0]} > shifted_energy

   #fi
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "Takes the difference between 2 single columned files"
   echo "   and expresses the output in terms of [meV/atom]  "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: diffE_perAtom.sh <file1> <file2>"
fi

