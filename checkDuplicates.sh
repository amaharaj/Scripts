#!/bin/bash

args=("$@")

sort ${args[0]} | uniq -d | grep -nFxf - ${args[0]}

