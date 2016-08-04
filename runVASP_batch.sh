#!/bin/bash

num=0
cd VASP_RUNS
for entry in `ls`; do
 
   cd $entry 
   head POSCAR
   # run vasp
   cd ../
   num=$(($num+1))

done
