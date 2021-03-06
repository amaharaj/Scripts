import numpy as np
import os, sys

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def parse_frc(mdfrc):
    """
    parse mdfrc file
    """
 
    fout = open('mdfrc.out', 'w+')
    with open('mdfrc','r') as fin:
        data = fin.readlines()

    # remove white spaces and newlines from data
    newdata = []
    for i in data:
       a = i.strip("\n")
       # since columns are set to be 8 characters wide,
       # split columns every 8 characters
       b = [a[_*8:(_+1)*8] for _ in range((len(a) / 8)) ]
       b = [_.strip() for _ in b ] 
       newdata.append(b)

    # flatten the list of lists
    forces = [val for sublist in newdata for val in sublist]
    
    # need to group forces into 3 and print Fx, Fy, Fz to single file
    for i in range(len(forces)):
        # if i mod 3 = 0 then print x component
        if (i%3==0):
            fout.write(str(forces[i]) + "      ")
        # if i mod 3 = 0 then print y component
        if (i%3==1):
            fout.write(str(forces[i]) + "      ")
        # if i mod 3 = 0 then print z component
        if (i%3==2):
            fout.write(str(forces[i]) + "\n ")

    fout.close()

def main():
    """
    This is the main function.
    """
    # A clean way to ask for user input
    try:
        # Attempt to retrieve required input from user
        prog = sys.argv[0]
        mdfrc = sys.argv[1]
    except IndexError:
        # Tell the user what they need to give
        print '\nusage: '+prog+' <mdfrc> \n'
        # Exit the program cleanly
        sys.exit(0)

    # Execute the function defined above

    forces = parse_frc(mdfrc)


# This executes cmain() only if executed from shell
if __name__ == '__main__':
    main()
