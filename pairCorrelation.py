import numpy as np
import os
import sys

# execute as: python pairCorrelation.py <file> <bin size>

def distanceCalc(names,x,z,y):
   for i in range(atoms):
      for j in range(i):
         print "j: ", j, str(names[j]) + str(i)+str(j)
         print "i: ", i, str(names[i]) + str(i)+str(j)
         print "====", 'end calculation', '===='
         print '\n'

xyz = sys.argv[1]
bin_size = sys.argv[2]
bin_size = int(bin_size)

xyz_read = open(xyz, 'r')

# parse xyz format

atoms = int(xyz_read.readline())
xyz_read.readline()

data = np.genfromtxt(xyz_read, delimiter='',dtype=None)

names = []
for i in range(atoms): names.append(data[i][0])
x = np.zeros(atoms)
y = np.zeros(atoms)
z = np.zeros(atoms)
for i in range(atoms):
   x[i] = data[i][1]
   y[i] = data[i][2]
   z[i] = data[i][3]
print "x: ", x
print "y: ", y 
print "z: ", z

distanceCalc(names,x,y,z)
