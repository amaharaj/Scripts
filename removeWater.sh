#!/bin/bash

args=("$@")

rm temp temp2 del out.pdb

# Input a pdb file, the number of molecules to be removed
# and number of atoms per molecule
pdbfile=${args[0]}
samples=${args[1]}
natoms=${args[2]}

if [[ $# -eq $natoms ]]
then 
   # Want the number of atoms in system so grep 'ATOM' from .pdb file
   grep 'ATOM' $pdbfile | wc -l > temp
   N=$(<temp)

   # Now divide by number of atoms per molecule to give number of molecules
   molecules=$((  $(grep 'ATOM' $pdbfile | wc -l )/$natoms  ))

   # 'ID' the molecules 
   for i in $(seq 1 $molecules); do echo $i >> temp2; done

   # Randomly select certain molecules to be removed from file and sort ID's
   shuf -n $samples temp2 > rnd
   sort -n rnd > sortrnd

   # Identify the range of lines which need to be deleted from .pdb file
   # eg. if molecule has 3 atoms, those 3 atoms and the 'TER' card are 
   # removed from the .pdb file (natoms + 1 lines are removed for each residue)
  # while read p; do
   #   for j in $(seq 0 $natoms)
    #  do 
     #    line=$(($p+$j))
      #   echo $line >> del
      #done 
   #done < sortrnd


   ### Needs fixing - prints lines to file p times ###
   ### currently turns flag on if the randomly selected molecule ### 
   ### is the same as the residue in the pdb file ###
   while read line; do 
      while read p; do
         lineCols=( $line )
         if [[ ${lineCols[4]} -eq $p ]]
         then 
            flag=1
            echo "${lineCols[4]}" 
         else 
            flag=0
         fi
         if [[ $flag -eq 1 ]]
         then 
            echo "hit"
         else
            echo $line >> out.pdb
         fi 
      done < sortrnd
   done < $pdbfile

   rm temp temp2 
 
   
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " Randomly removes a user-defined number of molecules "
   echo " NOTE: molecules must have the same number of atoms "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: removeWater.sh <pdbfile> <# of molecules to remove> <# of atoms / molecule>"
fi

