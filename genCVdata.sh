#!/bin/bash 

args=("$@")

#if [ ! -d xsf-cv ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
 #  mkdir xsf-cv
 #  echo "making xsf-cv directory..."
#fi

#if [ ! -d xsf-trn ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
#   mkdir xsf-trn
 #  echo "making xsf-train directory..."
#fi

#if [ ! -d xsf-tst ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
 #  mkdir xsf-tst
  # echo "making xsf-test directory..."
#fi

path_to_xsf=${args[0]}
file1=${args[1]}
file2=${args[2]}

genCV ()
{ 
rsync -avz --exclude-from <( echo $list_exclude ) $path_to_xsf xsf-cv
}

genTrain ()
{
rsync -avz --include-from <( echo $file1 ) $path_to_xsf xsf-trn
}

genTest ()
{
rsync -avz --include-from <( echo $file2 ) $path_to_xsf xsf-tst
}

if [[ $# -eq 3 ]]
then 
   list_exclude=$(cat $file1 $file2)
   genCV $list_exclude
   genTrain #xsf-train
   genTest #xsf-test
elif [[ $# -eq 2 ]]
then 
   list_exclude=${args[1]} 
   genCV #xsf-cv
   genTrain #xsf-train
   genTest #xsf-test
else
   echo " "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo "  Separate cross-validation data and store in xsf-cv     "
   echo "  folder. Provide list of train data, test data or both  "
   echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
   echo " "
   echo "Usage: genCVdata.sh <path-to-all-xsf-files> <Train Data> Optional: <Test Data>"
fi

