from ase.calculators.dftb import Dftb
from ase.io import write, read
from ase.build import molecule
import os, sys

def getForces(natoms, nconfigs, infile, outfile):
   """
   This function runs a point calculation using ASE's DFTB calculator and returns the 
   forces of a water structure. 
   NOTE: The input file will need to be zeropadded in xyz format.
   """

   #read in .xyz files one by one
   for i in range(nconfigs):

      numpad = str("%05d" % int(i))

      # read in structure: use xyz2struc code first
      system = read(infile + numpad + '.xyz')
      print '\n Performing point calculation on: ' + infile + numpad + '.xyz'
      print '--------------------------------------------------------------'

      # set up dftb calculator for optimization
      calc = Dftb(label='h2o', atoms=system,
            run_manyDftb_steps=True,
            Driver_='ConjugateGradient',
            Driver_MaxForceComponent='1E-4',
            Driver_MaxSteps=0,
            Hamiltonian_MaxAngularMomentum_='',
            Hamiltonian_MaxAngularMomentum_O='"p"',
            Hamiltonian_MaxAngularMomentum_H='"s"')
      system.set_calculator(calc)
      calc.calculate(system)

      # convert and rename output files
      os.system( 'xyz2gen geo_end.gen' )
      os.system( 'mv geo_end.xyz temp%s.xyz' % numpad )
      # write output files and move rename detailed out 
      os.system( 'mv detailed.out detailed.out%s' % numpad )
      # insert 2 lines at top of forces file
      os.system( 'echo \" \" > Forces%s' % numpad )
      os.system( 'echo \" \" >> Forces%s' % numpad )
      # get forces from detailed out using awk, write to Forces file
      os.system( 'awk \'/Total Forces/ { for(i=1; i<=' + str(natoms) + '; i++) {getline; print} }\' detailed.out%s >> Forces%s' % ( numpad , numpad ) )
      # combine coordinates and forces
      os.system( ('paste temp%s.xyz Forces%s >' + str(outfile) + '%s.xyz') % (numpad, numpad, numpad) )
      # clean up files
      os.system( 'rm detailed.out%s Forces%s temp%s.xyz' % ( numpad, numpad, numpad ) )  

def main():
   """
   This is the main function
   """
   # A clean way to ask for user input
   try:
      # Attempt to retrieve required input from user
      prog = sys.argv[0]
      natoms = int(sys.argv[1])
      nconfigs = int(sys.argv[2])
      infile = str(sys.argv[3])
      outfile = str(sys.argv[4])

   except IndexError:
      # Tell the user what they need to give
      print '\nUsage: '+prog+' <number of atoms> <number of configurations> <infile prefix> <outfile prefix> \n'
      # Exit the program cleanly
      sys.exit(0)

   getForces(natoms, nconfigs, infile, outfile)

if __name__=='__main__':
   main()

