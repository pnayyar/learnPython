name = "Tixdo"

if (name == "Tixdo"):
    print ("Welcome to", name)
elif(name == "Tixdo 1"):
    print ("not matched")
    pass
else:
    print("Welcome whoever") 

# list
name = "Pixdo"

if name in [ "Pixdo", "Tixdo"]:
    print ("Welcome to", name)
elif(name == "Pixdo"):
    print ("It will not come to this else")
    pass
else:
    print("Welcome whoever") 

#Dictionary
# list
name = "Fixdo"

if name in { "Fixdo": 1, "Pirxdo":2, "Tixdo":3}:
    print ("Welcome to", name)
elif(name == "Pixdo"):
    print ("It will not come to this else")
    pass
else:
    print("Welcome whoever")