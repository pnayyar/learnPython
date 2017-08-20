# Create a ToDo app, where -a for add , d for delete the option, -v for display

import os
import sys


if len(sys.argv) < 1:
    print("Error not sufficient arguments")
    sys.exit(1)

if len (sys.argv) >= 1:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            print ("File is not present, creating.. ",file_name )

try:
    if os.path.isfile(file_name):
        if  (sys.argv[2] == "-a"):
            with open(file_name, 'a') as f:
                print ("File getting appended")
                f.write(sys.argv[3] + " \n")
                n += 1
            
        elif (sys.argv[2] == "-v"):
            f = open(file_name, 'r')
            print("Reading ..\n ", f.read())
        
    #      elif (sys.argv[2] == "-d"):
    #          f = open(file_name, 'r')
    #          toBeDeleted = f.seek(eof - 1)
    #          tail -n +2 "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"
    #          print("Deleting ..", f.delete(sys.argv[3]))

        else:
            print ("Invalid Arguments")

except Exception as err:
    print (err) # This will print the exact error
    print("Error with arguments")

#finally:
 #   print("yay!! Todo app works !!")
                


 

    