def print_msg(msg, error="No Error", *args, **kwargs):
    print("Log : " +error+ " :" + msg)
    print(args, kwargs)

print_msg("This will be logged", "File not found", "a","b","c", key_1="1", key_2="5")# Kwrgs consider it as dic so if I give error="File not found", it will throw errroo as it is a

