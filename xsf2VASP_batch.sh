#!/bin/bash

mkdir VASP_RUNS

num=0
for entry in `ls`; do
 
   #atomsk $entry POSCAR
   run="$(printf "%05d\n" $num)" 
   mkdir VASP_RUNS/$run
   mkdir VASP_RUNS/$run/xsf
   cp $entry VASP_RUNS/$run/xsf
   atomsk $entry POSCAR
   mv POSCAR VASP_RUNS/$run
   
   num=$(($num+1))

done
