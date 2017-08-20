import sys
import os

#import pdb 
#pdb.set_trace()
if len(sys.argv) == 1:
    print("Error not sufficient arguments")
    sys.exit(1)

if len (sys.argv) >= 1:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            f.write("Written File")
            print ("File is written")

