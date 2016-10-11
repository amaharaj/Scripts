import numpy as np
import sys

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def readfiles(filename):
 
   lines = open(filename).read().splitlines()
   my_list = np.asarray(lines)

   natoms = int(lines[0])
   steps = (len(lines)/(natoms+2))

   new = np.reshape(my_list,(steps,(natoms+2)))
   
   #a = new.shape
   #print a[0]   

   X = np.delete(new,(0), axis=1)
   coords = np.delete(X,(0), axis=1)

   Prim_Vec1 = [0,0,0]
   Prim_Vec2 = [0,0,0]
   Prim_Vec3 = [0,0,0]
   energy = 0

   for i in range(steps):
      writefiles(Prim_Vec1, Prim_Vec2, Prim_Vec3, energy, natoms, coords[i],i)


def writefiles(Prim_Vec1, Prim_Vec2, Prim_Vec3, energy, natoms, coords,i):

   filename = open("structure"+str(i)+".xsf", 'w')
   filename.write("# total energy = " + str(energy) + " eV " + "\n")
   filename.write("\n" + "CRYSTAL" + "\n" + "PRIMVEC" + "\n")
   filename.write("        " + str(Prim_Vec1[0]) + "     " + str(Prim_Vec1[1]) + "     "  + str(Prim_Vec1[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec2[0]) + "     " + str(Prim_Vec2[1]) + "     "  + str(Prim_Vec2[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec3[0]) + "     " + str(Prim_Vec3[1]) + "     "  + str(Prim_Vec3[2]) + "     " + "\n" )
   filename.write("PRIMCOORD" + "\n")
   filename.write(str(natoms) + " " + str(1) + "\n")
   for i in range(len(coords)):
     
      filename.write(str(coords[i]) + "\n")
   filename.close()

def main():
   """
   This is the main function.
   """
   # A clean way to ask for user input
   try:
      # Attempt to retrieve required input from user
      prog = sys.argv[0]
      filename = sys.argv[1]
      #natoms = sys.argv[1]
      #atom_list = sys.argv[2]

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

   readfiles(filename)
   #Prim_Vec1, Prim_Vec2, Prim_Vec3, atomlist, energy, coords = readfiles(atom_list)

   #writefiles(Prim_Vec1, Prim_Vec2, Prim_Vec3, atomlist, energy, natoms, coords)
   # Execute the functions defined above

# This executes main() only if executed from shell
if __name__ == '__main__':
   main()


