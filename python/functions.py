def new_func(name):
    print("my name is "+name)
    
new_func("mustafa")    
print("-------------------")
#return functions
def mul(d,t):
    return d * t

print(mul(5,2))
print("----------------")
#assign value to parameters
#order doesnt matter
def func2(x1,x2,x3):
    print("the youngest child is " + x2)
    
func2(x2="omar", x1="ahmed",x3="kareem") 
print("----------------")
#default  value func
def func2(x = "fahd"):
    print("the youngest child is " + x)
    
func2("omar") 
func2() 
print("----------------")
#///////////////////////////
def func3(para):
    for n in para:
        print(n)
        
mylist = ["apple","banana","cherry"]
mytuple = (1,2,3)
func3(mylist)        
func3(mytuple)        
print("----------------")
#veridic function and assign parameter
def func4(*value):
    print("the first one is "+ value[2])
    
func4("ahmed","khaled","ali")    
print("----------------")
#lambda ///////////////
x = lambda a : a +10
print(x(3))
d = lambda f,s : f * s
print(d(5,4))
print("----------------")
