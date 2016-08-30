import numpy as np
import sys

def readfiles(atom_list):

   with open('XDATCAR','r') as f:

      f.readline()
      f.readline()
      vec_1 = f.readline()
      vec_2 = f.readline()
      vec_3 = f.readline()
      f.readline()
      f.readline()
      f.readline()
      coords = f.readlines()
   
      p1 = vec_1.split()
      p2 = vec_2.split()
      p3 = vec_3.split()

   Prim_Vec1 = []
   Prim_Vec2 = []
   Prim_Vec3 = []
   
   for i in range(3):
      vector1 = "p" + str(i) + "x"
      vector2 = "p" + str(i) + "y"
      vector3 = "p" + str(i) + "z"
      prim_vector1 =  "primvec" + str(i) + "x"
      prim_vector2 =  "primvec" + str(i) + "y"
      prim_vector3 =  "primvec" + str(i) + "z"
      prim_vector1 = p1[i]
      Prim_Vec1.append(prim_vector1)
      prim_vector2 = p2[i]
      Prim_Vec2.append(prim_vector2)
      prim_vector3 = p3[i]
      Prim_Vec3.append(prim_vector3)
   
   openfile = str(atom_list)
   with open(openfile,'r') as f2:

      atomlist = f2.readlines()

   with open('Energy','r') as f3:
   
      energy = f3.readlines()   

   return Prim_Vec1, Prim_Vec2, Prim_Vec3, atomlist, energy, coords

def writefiles(Prim_Vec1, Prim_Vec2, Prim_Vec3, atomlist, energy, natoms, coords):
   
   filename = open("structure.xsf", 'w')   
   filename.write("# total energy = " + str(energy[0]).rstrip() + " eV " + "\n")
   filename.write("\n" + "CRYSTAL" + "\n" + "PRIMVEC" + "\n")
   filename.write("        " + str(Prim_Vec1[0]) + "     " + str(Prim_Vec1[1]) + "     "  + str(Prim_Vec1[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec2[0]) + "     " + str(Prim_Vec2[1]) + "     "  + str(Prim_Vec2[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec3[0]) + "     " + str(Prim_Vec3[1]) + "     "  + str(Prim_Vec3[2]) + "     " + "\n" )
   filename.write("PRIMCOORD" + "\n")
   filename.write(str(natoms) + " " + str(1) + "\n")
   
   index = 0 
   for line in atomlist:
      filename.write(str(line[0]) + " " +str(coords[index]))
      index += 1

   filename.close()

def main():
   """
   This is the main function.
   """
   # A clean way to ask for user input
   try:
      # Attempt to retrieve required input from user
      prog = sys.argv[0]
      natoms = sys.argv[1]
      atom_list = sys.argv[2]

   except IndexError:
      # Tell the user what they need to give
      print ""
      print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
      print " NOTE: currently the user must provide a list of atom names"
      print " (separated by line) in order as they appear in XDATCAR file"
      print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
      print ""
      print '\nusage: '+prog+' <number of atoms> <atom list in order> \n'
      print ""
      # Exit the program cleanly
      sys.exit(0)
   
   Prim_Vec1, Prim_Vec2, Prim_Vec3, atomlist, energy, coords = readfiles(atom_list)

   writefiles(Prim_Vec1, Prim_Vec2, Prim_Vec3, atomlist, energy, natoms, coords)
   # Execute the functions defined above
  
# This executes main() only if executed from shell
if __name__ == '__main__':
   main()


