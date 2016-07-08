#!/bin/bash

args=("$@")

awk '{printf "%5.8f \n", $1*27.2114}' ${args[0]} > ${args[1]}
