import ase
from ase.io import read
import sys

filename = sys.argv[1]

coords = ase.io.read(str(filename), format='gen')

positions = []
outfile = open('test.POSCAR', 'w+')

O_count = 0
H_count = 0

print coords[-1]

for i in range(len(coords)):
   if coords[i].symbol == 'O':
      pos = str(coords[i].position[0]) + " " + str(coords[i].position[1]) + " " + str(coords[i].position[2]) + " O \n"
      positions.append(pos)
      O_count += 1
for i in range(len(coords)):
   if coords[i].symbol == 'H':
      pos = str(coords[i].position[0]) + " " + str(coords[i].position[1]) + " " + str(coords[i].position[2]) + " H \n"
      positions.append(pos)
      H_count += 1

outfile.write("O H \n")
outfile.write("1.000000\n")
outfile.write("27.2233508 0.0 0.0 \n")
outfile.write("0.0 27.1058073 0.0 \n")
outfile.write("0.0 0.0 27.0126432 \n")
outfile.write("O H \n")
outfile.write(str(O_count) + " " + str(H_count) + "\n")
outfile.write("Cartesian \n")
for i in range(len(positions)):
   outfile.write(str(positions[i]))
