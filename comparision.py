String = "I love Python"

#for i String:
 #   print i 

print(String[4:])
print(String[:4])
print(String[3:4])
print(String[:])
print(String[:-1])

myNewStringList = String.split(" ")
print(String[:].join(String.split()).split(":"))  ## Check how this works