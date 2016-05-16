#!/usr/bin/env python

# Convert back from reduced cell

import os, sys
import numpy as np

def read_file(script,lattice_vectors):
   xyz_read = open (script, 'r')
   atoms = int(xyz_read.readline())
   xyz_read.readline()
   data = np.genfromtxt(xyz_read, delimiter='',dtype=None)
   ntimes = len(data)
   names = []
   for i in range(ntimes): names.append(data[i][0])
   dim_r = (len(data),3)
   r = np.zeros(dim_r)
   for i in range(ntimes):
      r[i][0] = data[i][1]
      r[i][1] = data[i][2]
      r[i][2] = data[i][3]
   latt_vec = np.genfromtxt(lattice_vectors, delimiter='',dtype=None)
   return r, atoms, latt_vec, names, ntimes

def matrix_multiply(matrix1,matrix2):
   matrix_out = np.dot(matrix1,matrix2)
   return matrix_out

def write_file(reshaped_coords, names, atoms, ntimes):
   resized = open('Out.xyz','w')
   A = zip(names,reshaped_coords)
   resized.write(str(atoms) + '\n')
   resized.write('#comment' + '\n')
   for i in range(ntimes):
      resized.write(A[i][0] + " ")
      resized.write(str(A[i][1][0]) + " " + str(A[i][1][1]) + " " + str(A[i][1][2]))
      resized.write('\n')
 
def main():
   """
   This is the main function.
   """
   # A clean way to ask for user input
   try:
      # Attempt to retrieve required input from user
      prog = sys.argv[0]
      script = sys.argv[1]
      lattice_vectors = sys.argv[2]  
   except IndexError:
      # Tell the user what they need to give
      print '\nusage: '+prog+' <script> <lattice vectors> \n'
      # Exit the program cleanly
      sys.exit(0)

   # Execute the function defined above
   r, atoms, latt_vec, names, ntimes = read_file(script, lattice_vectors)
   reshaped_coords = matrix_multiply(r,latt_vec)
   write_file(reshaped_coords,names,atoms,ntimes)

# This executes cmain() only if executed from shell
if __name__ == '__main__':
    main()
