#!/bin/bash

# run as ./energyDifference.sh <file> <outfile>
# <file> must be a single column of numerical values

args=("$@")

awk 'NR>1{printf "%5.8f \n", $1-p } {p=$1}' ${args[0]} > ${args[1]}
