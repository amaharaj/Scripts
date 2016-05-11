from mpmath import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import sys

# written for 2 atomic species
# execute as: python pairCorrelation.py <file> 

# function to calculate distance between pairs
def distanceCalc(names,x,z,y,A,B):
   for i in range(atoms):
      for j in range(i):
         # vector between atoms
         dx = x[j]-x[i]
         dy = y[j]-y[i]
         dz = z[j]-z[i]
         # minimum image correction
         dx = dx - nint(dx / cell_x)*cell_x
         dy = dy - nint(dy / cell_y)*cell_y
         dz = dz - nint(dz / cell_z)*cell_z
         distance = sqrt(dx*dx + dy*dy + dz*dz)
         # append different pair combination arrays
         if names[i] == names[j] and names[i] == str(A):
            AA.append(distance)
         elif names[i] == names[j] and names[i] == str(B):
            BB.append(distance)
         else: 
            AB.append(distance)

# read in command line arguments
xyz = sys.argv[1]
bin_size = raw_input('Enter Bin Size: ').split()
cell = raw_input('Enter Parameters for Periodic Cell <cell length x> <cell length y> <cell length z>: ').split()
bin_size = int(bin_size[0])
cell_x = float(cell[0])
cell_y = float(cell[1])
cell_z = float(cell[2])

xyz_read = open(xyz, 'r')

# parse xyz format
atoms = int(xyz_read.readline())
xyz_read.readline()
data = np.genfromtxt(xyz_read, delimiter='',dtype=None)

names = []
AA = []
BB = []
AB = []

# fill name and coordinate arrays
for i in range(atoms): names.append(data[i][0])
x = np.zeros(atoms)
y = np.zeros(atoms)
z = np.zeros(atoms)
for i in range(atoms):
   x[i] = data[i][1]
   y[i] = data[i][2]
   z[i] = data[i][3]

# sort atomic name list and store first and last element in A and B respectively
# one atomic species is labelled A, the other is labelled B
names = sorted(names)
A = names[0]
B = names[-1]
distanceCalc(names,x,y,z,A,B)

# plot histogram (frequency of pair combinations)
n, bins, patches = plt.hist((AA,BB,AB),bin_size,normed=1,alpha=0.75,label=[str(A)+"-"+str(A),str(B)+"-"+str(B),str(A)+"-"+str(B)])
plt.legend()
plt.xlabel('Distances Between Pairs $\AA$')
plt.ylabel('Frequency of Pair Combinations')
plt.title('Pair Correlation Data')
plt.grid(True)

plt.show()

