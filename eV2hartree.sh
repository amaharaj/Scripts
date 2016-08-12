#!/bin/bash

# converts eV to hartree of a single columned file
# usage: eV2hartree <file in eV> <file in hartree>

args=("$@")

awk '{printf "%5.8f \n", $1/27.2114}' ${args[0]} > ${args[1]}

