#!/bin/bash

# test submit script: executes submission for a certain run and then kills it after 15s
# use in conjunction with xsf2VASP_batch.sh (this code generates run directories based
# on xsf files. xsf files are converted to POSCARs) 
# currently need VASP_RUNS folder to only contain run directory entries 
# i.e. can not have miscellaneous files in VASP_RUNS

num=0
cd VASP_RUNS
for entry in `ls`; do
 
   cd $entry 
   head POSCAR
   # run vasp
   timeout 15s nohup mpirun -n 4 ~/bin/vasp > output.log &
   echo "starting run: $num"
   wait 
   cd ../
   num=$(($num+1))

done
