from mpmath import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import sys

# written for 2 atomic species
# execute as: python pairCorrelation.py <file> <bin size> <cell length x> <cell length y> <cell length z>

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

# finds the maximum value of 3 variables
def maxLength(a,b,c):
   Max = a
   if b > Max:
      Max = b
   elif c > Max:
      Max = c
   return Max

# read in command line arguments
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
# use the longest length of box as the maximum distance between pairs
x = maxLength(cell_x,cell_y,cell_z)


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
n, bins, patches = plt.hist((AA,BB,AB),bin_size,normed=1,alpha=0.75)
#n, bins, patches = plt.hist(BB,bin_size,facecolor='blue', alpha=0.75)
#n, bins, patches = plt.hist(AB,bin_size,facecolor='red', alpha=0.75)

plt.xlabel('Distances Between Pairs $\AA$')
plt.ylabel('Frequency of Pair Combinations')
plt.title('Pair Correlation Data')
plt.grid(True)

plt.show()

