import numpy as np
import sys

# input arguments
filename=sys.argv[1]
natoms = sys.argv[2]
nsamples = sys.argv[3]

# Read in file
header = np.genfromtxt(filename, dtype=str, delimiter='\n', skip_footer=5+int(natoms))
atom_type = np.core.defchararray.split(header)
latvec = np.genfromtxt(filename, skip_header=2, skip_footer=2+int(natoms))
specs = np.genfromtxt(filename, dtype=str, delimiter='\n', skip_header=5, skip_footer=int(natoms))
natoms = np.core.defchararray.split(specs)
coords = np.loadtxt(filename, skiprows=7, usecols=(0,1,2))

lv = open('lvec', 'w+')

def reset():
   #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   #""" Reset coordinates and lattice vectors to original values """
   #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   # get coordinates and recast array as floats
   x =1.0*coords[:,0].astype(float)
   y = 1.0*coords[:,1].astype(float)
   z = 1.0*coords[:,2].astype(float)
   # get lattice vectors and recast array as floats
   lv_x = 1.0*latvec[:,0].astype(float)
   lv_y = 1.0*latvec[:,1].astype(float)
   lv_z = 1.0*latvec[:,2].astype(float)

   return x, y, z, lv_x, lv_y, lv_z

# Define a scaling factor that will scale the system by +-10%
scale_factor = np.linspace(-0.1,0.1,nsamples)

for i in range(len(scale_factor)):
   # Reset coordinates and lattice vectors
   x, y, z, lv_x, lv_y, lv_z = reset()
   
   # Scale coordinates and lattice vectors
   x*=(1.0+float(scale_factor[i]))
   y*=(1.0+float(scale_factor[i]))
   z*=(1.0+float(scale_factor[i]))
   lv_x*=(1.0+float(scale_factor[i]))
   lv_y*=(1.0+float(scale_factor[i]))
#   lv_z*=(1.0+float(scale_factor[i]))

   """ Write POSCAR files """
   
   f = open('out' + str("%05d" % i) + ".POSCAR", 'w+')
   # Write Header
   f.write(str(header[0]) + '\n' + str(header[1]) + '\n')
   # Write Transformed Lattice Vectors
   for j in range(len(latvec)):
      #f.write(str(latvec[i,0]) + '\t' + str(latvec[i,1]) + '\t'+ str(latvec[i,2]) + '\n')
      f.write('%.12f   %.12f   %.12f \n' % (lv_x[j], lv_y[j], lv_z[j]))
   # Write Specifications
   f.write(str(specs[0]) + '\n' + str(specs[1]) + '\n')
   # Write Transformed Coordinates
   for j in range(len(coords)):
      f.write('%.12f   %.12f   %.12f \n' % (x[j],y[j],z[j]))
   f.close()
 

   """ Write xyz files """

   f2 = open('out' + str("%05d" % i) + ".xyz", 'w+')
   f2.write(str(len(coords)) + '\n' + '\n')
   for j in range(int(natoms[0][0])):
      f2.write('%2s   %.12f   %.12f   %.12f \n' % (atom_type[0][0], x[j],y[j],z[j]))
   for j in range(int(natoms[0][1])):
      j += int(natoms[0][0])
      f2.write('%2s   %.12f   %.12f   %.12f \n' % (atom_type[0][1], x[j],y[j],z[j]))
   f2.close()

   """ Write gen files """
   # Note: Only implemented for binary systems with periodic boundaries 

   f3 = open('out' + str("%05d" % i) + ".gen", 'w+')
   f3.write(str(len(coords)) + ' S ' +  '\n' )
   f3.write(str(header[0]) + '\n')
   # n will specify atom 1 or 2
   n = 0
   for j in range(len(coords)):
      f3.write('    ' + str(j+1) + '\t')
      # Write 1 if first atom type
      if (n < (int(natoms[0][0]))):
         f3.write('1 \t')
         n += 1
      else:
      # Write 2 if second atom type
         f3.write('2 \t')
      f3.write('%.12f   %.12f   %.12f \n' % (x[j],y[j],z[j]))
   # Add lattice vectors
   f3.write('0.0 0.0 0.0 \n')
   for j in range(len(latvec)):
      f3.write('%.12f   %.12f   %.12f \n' % (lv_x[j], lv_y[j], lv_z[j]))
   f3.close()

   for j in range(len(latvec)):
      lv.write('%.12f   %.12f   %.12f \n' % (lv_x[j],lv_y[j],lv_z[j]))

lv.close()
