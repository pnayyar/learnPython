list1 = [10,20,30,40,50]
print(dir(list1))
list1.append(100)
print("\n", list1) 

list1.pop() 
print("\n", list1.pop(3)) #removes the element at that postion
print("\n", list1) 

#Hash , dictionary
d = {'one': 1, 'two':2}
print("Printing first and second element of a dictionary", d['one'], d['two'])
d['third'] = 3

print("Printing the whole dictionary", d)
