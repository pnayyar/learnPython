#wwc-variableType.py
# Use Ctrl + B to execute this code

myVarName = "Prachi"
print (type(myVarName))
myVarName = 123
print (type (myVarName))
myVarName = 3.41
print (type(myVarName))


def myFunction(myVarName):
	print ('Passing vairable to the function : Lets see what is the last value in the variable', myVarName)

myFunction(123)

def myFunction2(myVarName = 333):
	print ('Passed value runtime', myVarName)

myFunction2()

def myFunction3(myVarName = 333):
	a=10*myVarName
	return a

#myFunction3(10)
print ('value of a', myFunction3 (10))
print ('value of a with default value', myFunction3 ())

#multiple arguments
def myFunction4(var1, var2 = 0):
	sum = var1 + var2
	return sum

#myFunction3(10)
total = myFunction4(3,10)
print ('total =', total)

# passing hundered numbers or 15 numbers, use range
def func5(counter):
		for count in counter:
			print count

func5(range(2))

# 
def func6(*args, **kwargs):  #here * is for positional arguments as tupple of all the arguments and ** is for individual arguments, it will creates a dictionary of each arguments with key value pair
# NOTE: every keyword argument will come afer positional arguments

	print ('print all args and its type', args, type(args))
	print ('print all keyword args and its type', kwargs, type(kwargs))
	print ('args', args[3])
	print ('kwargs', kwargs['c'])
	#kwargs[a] = 100
	#print kwargs[a]

func6(1,2,3,4,5,6,a = 5, c = 9)


def func7(*args):
	print ('print args', args, type(args))
	print ('print 0th element args[0]', args[0], type(args[0]))
	print ('print args[0][3]', args[0][3], type(args[0][0]) )
	print ('print the list', args[0][:-1:3])  # [start:stop:step] here it iwll jump by 3

func7(range(20))

def passfunc():
	pass  # if u want to pass for now, usee pass

def func8(**kwargs):
	print ('print kwargs', kwargs, type(kwargs))
	print ('print 0th element kwargs[a]', kwargs['a'], type(kwargs['a']))
	
func8(a=20, b =20)

# Lambda function
# lambda should return something

# this is what lambda function do ..
# def lamdaFunc(x):
#	return x+1

a = lambda x:x+1 # here x is the argument for the function and x+1 is the return
print ("lamba print ", a(2))

# map function
#map(function, interative structure) it will call the function in iterative manner for that function
def boom(a):
	return a+100

a = map(boom, [2,5]) # it will call boom function 2 times
print ('Boom is called with 2 and 5 as arguments of a', a)


a = map(boom, (5,6)) # it will call boom function 2 times
print ('Boom is called with 5 and 6 as arguments of a', a)

a = map(boom, range(10)) # it will call boom function 2 times
print ('Boom is called with range of 10 as arguments of a', a)

# how to use map with lambda
print ('Combining the map and lambda function together in one line', map(lambda x:x+100, [2,5, 8]))
# here what we did with boom function is now done in one line with lambda function , calling the same function 3 times, with arguments 2 , 5 and 8 passed respectively

print ('Combining the map and lambda function together in one line', map(lambda x:(x*x-x+100), [2,5, 8]))

print ('Combining the map and lambda function together in one line', map(lambda x:x+100 if x < 10 else x + 1000, [2, 15, 18])) # inlambda it should always return something, so an else is compulsory

#map as identity function, functions which return u the same things are called identity functions
print (map(None, [1,2,3]))

# print even numbers

print ('Printing all even numbers from 1 to 10', map(lambda num:num  if num%2==0 else None, range(10)))
print ('Printing all even numbers from 1 to 10', map(lambda num:num  if num%2==0 else ' ', range(10)))
 # to avoid the None values, use Filters
print ('Printing all odd numbers from 1 to 10 using filters ', filter(lambda num:num%2,range(10)))
# using same with list
print ('Printing all even numbers from 1 to 10', [x for x in range(10) if x%2==0])  # Everything in [] is a list comprehension

# finding square of all odd numbers in a list
OddList = filter(lambda num:num%2,range(10))
print ('square of all Odd numbers in two lines', map(lambda num:num*num, OddList))

#same done in one line, first filter the add numbers using filter, then give map function to do the squaring
print ('square of all Odd numbers in one Line', map(lambda num:num*num, filter(lambda num:num%2,range(10))))

# make the above a little more complex
print ('cube of numbers less than 10 and square of numbers greater than 10, for all Odd numbers in one Line', map(lambda num:num*num*num if num<10 else num*num, filter(lambda num:num%2,range(10))))




