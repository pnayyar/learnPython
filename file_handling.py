# file operations

file_name = "myTasks.txt"

with open(file_name, 'w') as f:
    f.write("1. Attend the meetup")
    f.write("\n 2. Go home and get sleep" )
    f.write("\n 3. Make sure you had lunch before going")
    #  f.close() // you dont need this when using 'with' else f = open(file_name) will require a f.close
        

print ("File written successfully")

with open(file_name, 'a') as f:
    f.write("\n File appended")
    print ("File appended succesfully")

with open(file_name, 'r') as f:
    s = f.seek(2)
    print (s, "Seeked") # it returns the position at which it returns the position