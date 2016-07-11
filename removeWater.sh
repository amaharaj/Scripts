#!/bin/bash

args=("$@")

rm temp temp2 del out*.pdb reorder residue sortrnd rnd Removed_Residues

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

   NR=0
   skip=0
   delTER=0

   echo " " >> residue
   echo " " >> reorder 
   while read line; do
      counter=0 
      lineCols=( $line )
      while read p; do
       #  lineCols=( $line )
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
         echo "Deleting Residue" >> Removed_Residues
         echo $line >> Removed_Residues
      else
         echo $line >> out.pdb 
      fi 
   done < $pdbfile

   # Reorder and rename residues
   awk 'FNR==NR{a[NR]=$1;next}{$5=a[FNR]}1' residue out.pdb > out2.pdb
   awk 'FNR==NR{a[NR]=$1;next}{$2=a[FNR]}1' reorder out2.pdb > out3.pdb

   # Remove last line and replace with "END"
   sed -i '$ d' out3.pdb 
   echo "END" >> out3.pdb 

   # use printf to properly format the .pdb file. Note that the spaces are place holders for where 
   # there may be information in a pdb file. This may need modification for other .pdb files.
   awk '{printf "%-6s %4s %3s %4s %5s %3s %7s %7s %7s %5s %5s %9s %1s\n", $1, $2, $3, $4, $5, "   ", $6, $7, $8, $9, $10, "         ", $11}' out3.pdb > out.pdb

   rm temp temp2 out2.pdb out3.pdb temp temp2 del reorder residue rnd sortrnd
   
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "  Randomly removes a user-defined number of molecules    "
   echo "  NOTE: Molecules must have the same number of atoms     "
   echo " Ensure there are spaces separating each column in input "
   echo " May need to delete last digit in each of the coordinates"
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: removeWater.sh <pdbfile> <# of molecules to remove> <# of atoms / molecule>"
fi

