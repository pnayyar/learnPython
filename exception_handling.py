
i = 10
try:
    #j = i / 2
    j = i / 0
    print(j)
    print("This is printed")
except Exception as err:
    print (err) # This will print the exact error
    print("Error .")
finally:
    print("Finally this is executed, despite of try or error")