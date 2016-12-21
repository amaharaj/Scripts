#!/bin/bash 

args=("$@")

path_to_xsf=${args[0]}
# remove trailing slash if there is one
path_to_xsf=${path_to_xsf%/}
trn=${args[1]}
tst=${args[2]}

genCV ()
{ 
rsync -avz --exclude-from 'list_exclude' $path_to_xsf xsf-cv
#for file in $(<list_exclude); do cp "$path_to_xsf/!($file)" xsf-cv; done
}

genTrain ()
{
for file in $(<$trn); do cp "$path_to_xsf/$file" xsf-trn; done
}

genTest ()
{
for file in $(<$tst); do cp "$path_to_xsf/$file" xsf-tst; done
}

if [[ $# -eq 3 ]]
then 
   #list_exclude=$(cat $file1 $file2)
   cat $trn $tst > list_exclude
   genCV 
   genTrain
   genTest 
elif [[ $# -eq 2 ]]
then 
   list_exclude=${args[1]} 
   genCV 
   genTrain 
   genTest 
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "  Separate cross-validation data and store in xsf-cv     "
   echo "  folder. Provide list of train data, test data or both  "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: genCVdata.sh <path-to-all-xsf-files> <Train Data> Optional: <Test Data>"
fi

