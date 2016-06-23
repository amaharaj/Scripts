#!/bin/bash

# runs sander NOTE: overwrites previous files
# Usage: ./runAMBER.sh <inpcrd> <rst> (optional) <mdcrd>

args=("$@")

if [[ $# -eq 2 ]] 
then 
    $AMBERHOME/bin/sander -O -i mdin -o mdout -p prmtop -c ${args[0]} -r ${args[1]}
fi
if [[ $# -eq 3 ]]
then
    $AMBERHOME/bin/sander -O -i mdin -o mdout -p prmtop -c ${args[0]} -r ${args[1]} -x ${args[2]}
fi
if [[ $# -eq 0 ]]
then
    echo "Runs AMBER using Sander"
    echo " " 
    echo "~~~~~ Label files as specified: ~~~~~~~"
    echo "input file: mdin"
    echo "output file: mdout "
    echo "parameter/topology file: prmtop"
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo " " 
    echo "Usage: ./runAMBER.sh <inpcrd> <rst> (optional: <mdcrd>)"
fi

