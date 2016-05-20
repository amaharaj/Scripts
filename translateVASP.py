import ase.io
import ase.io.vasp 

cell = ase.io.vasp.read_vasp('POSCAR')

ase.io.vasp.write_vasp('outfile',cell*(3,3,3),direct=True,sort=True)

