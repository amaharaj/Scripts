#!/bin/bash

# Converts energy to eV from Hartrees, and forces from Hartree/Bohr to eV/Angstrom

for entry in `ls convert_xsf/`; do
   # store total energy in hartrees
   EHartree="$(awk 'NR==1 {print $5}' convert_xsf/$entry)"
   # store total energy in eV
   EEv="$(awk 'NR==1 {printf "%5.8f", $5*27.211396}' convert_xsf/$entry)"
   echo "${EEv}"
   # convert total energy in place to eV
   # 1 eV = 27.211396
   sed -i "s/${EHartree}/${EEv}/g" convert_xsf/$entry 
   # convert forces in place to eV/Angstrom
   # 1 Hartree/Bohr = 51.42208619 eV/Angstrom
   awk -F" "  '(NR<10){print $0}NR>10{printf "%3s %5.8f %5.8f %5.8f %5.8f %5.8f %5.8f\n", $1, $2, $3, $4, $5*51.42208619, $6*51.42208619, $7*51.42208619}' convert_xsf/$entry | sponge convert_xsf/$entry    
done 

