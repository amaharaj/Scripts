#!/bin/bash

for entry in `ls OUTPUT/`; do 

   cp atomlist OUTPUT/$entry 
   cd OUTPUT/$entry 
   # run conversion script
   python ../../xdatcar2xsf.py 300 atomlist
   # get name of current directory only
   dir=`basename $PWD`
   # rename strucure file based on directory number
   mv structure.xsf structure$dir.xsf
   cd ../../
     
done

