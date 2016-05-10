from mpmath import *
import numpy as np
import os
import sys

# written for 2 atomic species
# execute as: python pairCorrelation.py <file> <bin size> <cell length x> <cell length y> <cell length z>

def distanceCalc(names,x,z,y,A,B):
   for i in range(atoms):
      for j in range(i):
         print "j: ", j, str(names[j]) + str(i)+str(j)
         print "i: ", i, str(names[i]) + str(i)+str(j)
         print "====", 'end calculation', '===='
         print '\n'
         # vector between atoms
         dx = x[j]-x[i]
         dy = y[j]-y[i]
         dz = z[j]-z[i]
         # minimum image correction
         dx = dx - nint(dx / cell_x)*cell_x
         dy = dy - nint(dy / cell_y)*cell_y
         dz = dz - nint(dz / cell_z)*cell_z
         distance = sqrt(dx*dx + dy*dy + dz*dz)
         if names[i] == names[j] and names[i] == str(A):
            print "A-A pair"
            AA.append(distance)
         elif names[i] == names[j] and names[i] == str(B):
            print "B-B pair"
            BB.append(distance)
         else: 
            print "A-B pair"
            AB.append(distance)

xyz = sys.argv[1]
bin_size = int(sys.argv[2])
cell_x = int(sys.argv[3])
cell_y = int(sys.argv[4])
cell_z = int(sys.argv[5])

xyz_read = open(xyz, 'r')

# parse xyz format

atoms = int(xyz_read.readline())
xyz_read.readline()

data = np.genfromtxt(xyz_read, delimiter='',dtype=None)

names = []
AA = []
BB = []
AB = []

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

#distanceCalc(names,x,y,z)
print sorted(names)
A = names[0]
B = names[-1]
print A, B
distanceCalc(names,x,y,z,A,B)
print AB
print AA
print BB
