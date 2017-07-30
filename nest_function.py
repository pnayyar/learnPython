def hello_work():
    def hello_work2():
        print("Hello work 2")

    print("Hello work1") 
    hello_work2()

hello_work()
#hello_work2() //Since this is nested, it will not work, its scope is till the parent function only
 
def hello_world():
    print("Hello work1") 
    
def hello_world2():
        print("Hello world 2")
        hello_world()
    
print("Calling hellow world2 "), hello_world2()

print("Calling hellow world2 "), hello_world()

 