import sys
import numpy as np 

# script to generate evenly spaced points over some range 
# evaluated on a lennard jones potential 
# generates LennardJones.txt 

# execute as `python lennard.py <number of points to evaluate>`

outfile = open('LennardJones.txt','w+')

divisions = sys.argv[1]

def lennardJones(r, r_m, e):
   VLJ = np.zeros(len(r))
   VLJ = e*((r_m/r)**12 - 2*(r_m/r)**6)
   return VLJ

# generate distance values between some range
r = np.linspace(1.0,2.0,divisions)

VLJ = lennardJones(r,r_m=1.22,e=10)

for i in range(len(r)): 
   # print distance then potential evaluated at that distance to file
   outfile.write(str(r[i]) + " " + str(VLJ[i]) + "\n")

outfile.close()
