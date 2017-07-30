def print_msg(msg, error="No Error", *kwargs):
    print("Log : " +error+ " :" + msg)
    print(kwargs)

print_msg("This will be logged", "File not found", "1","2","3","4","5") # Kwrgs consider it as dic so if I give error="File not found", it will throw errroo as it is a

