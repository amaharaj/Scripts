#!/bin/bash

args=("$@")

rm temp temp2 del out.pdb reorder residue

# Input a pdb file, the number of molecules to be removed
# and number of atoms per molecule
pdbfile=${args[0]}
samples=${args[1]}
natoms=${args[2]}

if [[ $# -eq 3 ]]
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

   ### Needs fixing - prints lines to file p times ###
   ### currently turns flag on if the randomly selected molecule ### 
   ### is the same as the residue in the pdb file ###
   NR=0
   skip=0
   delTER=0
   echo " " >> residue
   echo " " >> reorder 
   while read line; do
      counter=0 
      while read p; do
         lineCols=( $line )
         # if all atoms in molecule of molecule have been deleted 
         # delTER will be equal to the number of atoms
         # turn on the flag and reset counter then skip the line
         if [[ $delTER -eq $natoms ]]
         then
            flag=1
            delTER=0 
            break
         fi 
         # if residue number is equal to the randomly selected 
         # molecule turn on the flag and update the delTER counter
         if [[ ${lineCols[4]} -eq $p ]]
         then 
            flag=1
            echo "${lineCols[4]}" 
            delTER=$(($delTER+1))
            break
         else 
         # if the residue is not being deleted, update files to 
         # reorder atoms and residues
            flag=0
            if [[ $counter -eq 1 ]] 
            then 
               NR=$(($NR+1))
               if [[ $(($NR%4)) -eq 0 ]]
               then
                  echo " " >> reorder
                  skip=$(($skip+1))
                  echo " " >> residue
               else
                  RES=$(($skip+1))
                  echo $(($NR-$skip)) >> reorder
                  echo $RES >> residue
               fi
            fi 
            counter=$(($counter+1)) 
         fi 
      done < sortrnd
      # Write to output file if flag is off
      # Skip line if flag is on
      if [[ $flag -eq 1 ]]
      then
         echo "Deleting Residue"
         echo $line
      else
         echo $line >> out.pdb 
      fi 
   done < $pdbfile

   awk 'FNR==NR{a[NR]=$1;next}{$5=a[FNR]}1' residue out.pdb > out2.pdb
   awk 'FNR==NR{a[NR]=$1;next}{$2=a[FNR]}1' reorder out2.pdb > out3.pdb

   sed -i '$ d' out3.pdb 
   echo "END" >> out3.pdb 

   mv out3.pdb out.pdb

   rm temp temp2 out2 
 
   
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " Randomly removes a user-defined number of molecules "
   echo " NOTE: molecules must have the same number of atoms "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: removeWater.sh <pdbfile> <# of molecules to remove> <# of atoms / molecule>"
fi

