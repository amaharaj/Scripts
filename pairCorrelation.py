from mpmath import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import os
import sys

# computes pair correlation function and expresses as a histogram

def read_file(script, bins, cell_x, cell_y, cell_z):
   #parse xyz format
   xyz_read = open(script, 'r')
   atoms = int(xyz_read.readline())
   xyz_read.readline()
   data = np.genfromtxt(xyz_read, delimiter='',dtype=None)
   # fill name and coordinate arrays
   ntimes = len(data)/atoms
   names = []
   for i in range(atoms): names.append(data[i][0])
   dim = (len(data),3)
   r = np.zeros(dim)
   for i in range(len(data)):
      r[i][0] = data[i][1]
      r[i][1] = data[i][2]
      r[i][2] = data[i][3]
   r = r.reshape((ntimes,atoms,3)) 
   # sort atomic name list and store first and last element in A and B respectively
   # one atomic species is labelled A, the other is labelled B
   names = sorted(names)
   A = names[0]
   B = names[-1]
   lattice_vectors = [ [cell_x,0.0,0.0], [0.0, cell_y,0.0], [0.0,0.0,cell_z]]

   return lattice_vectors, atoms, names, A, B, r, ntimes

def distance_pbc(r_i,r_j,lattice_vectors):
   # vector between atoms
   dx = r_i[0]-r_j[0]
   dy = r_i[1]-r_j[1]
   dz = r_i[2]-r_j[2]
   cell_x = lattice_vectors[0][0]
   cell_y = lattice_vectors[1][1]
   cell_z = lattice_vectors[2][2]

   # minimum image correction
   dx = dx - nint(dx / cell_x)*cell_x
   dy = dy - nint(dy / cell_y)*cell_y
   dz = dz - nint(dz / cell_z)*cell_z
   distance = sqrt(dx*dx + dy*dy + dz*dz)
   return distance  

def distanceCalc(lattice_vectors,atoms,names,r,A,B):

   AA = []
   BB = []
   AB = []

   for i in range(atoms):

      for j in range(i):

         r_i = r[i]
         r_j = r[j]

         distance = distance_pbc(r_i,r_j,lattice_vectors)

         # append different pair combination arrays
         if names[i] == names[j] and names[i] == str(A):
            AA.append(distance)
         elif names[i] == names[j] and names[i] == str(B):
            BB.append(distance)
         else: 
            AB.append(distance)
   return AA, BB, AB


def make_histogram(bins,rho,AA,BB,AB,A,B,ntimes):
   # Plot Radial Distribution Function
   hist1,r = np.histogram(AA,bins,normed=True)
   hist2,r = np.histogram(BB,bins,normed=True)
   hist3,r = np.histogram(AB,bins,normed=True)
   normalization_factor = np.zeros(int(bins)) 
   for i in range(int(bins)):
      normalization_factor[i] = float(1/( (4*math.pi*r[i]**2) * rho * (float(max(r)/bins)) ))
   histAA = np.multiply(hist1,normalization_factor)
   histBB = np.multiply(hist2,normalization_factor)
   histAB = np.multiply(hist3,normalization_factor)
   plt.plot(r[1:],histAA,"-",label=str(A)+"-"+str(A))
   plt.plot(r[1:],histBB,"-",label=str(B)+"-"+str(B))
   plt.plot(r[1:],histAB,"-",label=str(A)+"-"+str(B))
   plt.legend()
   plt.xlabel('Distances Between Pairs $\AA$')
   plt.ylabel('Frequency of Pair Combinations')
   plt.title('Pair Correlation Data')
   plt.grid(True)

   plt.show()



def main():
   """
   This is the main function.
   """
   # A clean way to ask for user input
   try:
      # Attempt to retrieve required input from user
      prog = sys.argv[0]
      script = sys.argv[1]
      bins = float(sys.argv[2])
      cell_x = float(sys.argv[3])
      cell_y = float(sys.argv[4])
      cell_z = float(sys.argv[5])
      
   except IndexError:
      # Tell the user what they need to give
      print '\nusage: '+prog+' <.xyz file> <number of bins> <cell length x> <cell length y> <cell length z> \n'
      # Exit the program cleanly
      sys.exit(0)

   # Execute the functions defined above
   lattice_vectors,atoms,names,A,B,r,ntimes = read_file(script,bins,cell_x,cell_y,cell_z)
   for i in range(len(r)):
      AA,BB,AB = distanceCalc(lattice_vectors,atoms,names,r[i],A,B)
   rho = float(atoms)/(cell_x*cell_y*cell_z)
   make_histogram(bins,rho,AA,BB,AB,A,B,ntimes)

# This executes main() only if executed from shell
if __name__ == '__main__':
   main()
