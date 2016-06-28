import sys
import numpy as np 


outfile = open('LennardJones.txt','w+')

divisions = sys.argv[1]

def lennardJones(r, r_m, e):
   VLJ = np.zeros(len(r))
   VLJ = e*((r_m/r)**12 - 2*(r_m/r)**6)
   return VLJ

r = np.linspace(1.0,2.0,divisions)

VLJ = lennardJones(r,r_m=1.22,e=10)

for i in range(len(r)): 
   outfile.write(str(r[i]) + " " + str(VLJ[i]) + "\n")

outfile.close()
