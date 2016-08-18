#!/bin/bash

args=("$@")

mdcrd=${args[0]}
xyz=${args[1]}

if [[ $# -eq 2 ]]
then

   cpptraj -p prmtop -y $mdcrd -x temp.pdb
   babel -ipdb temp.pdb -oxyz $xyz
else
    echo " "
    echo "Converts mdcrd to xyz file using cpptraj and openbabel "
    echo " " 
    echo "~~~~~~~~~~~~~ label files as specified: ~~~~~~~~~~~~~~~"
    echo "parameter/topology file: prmtop"
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo " " 
    echo "Usage: ./mdcrd2xyz.sh <*.mdcrd> <*.xyz>         "
fi 
