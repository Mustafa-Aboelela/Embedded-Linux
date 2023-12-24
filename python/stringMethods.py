#strip()  remove any spaces from begging or end

x =  " mustafa mohamed "
print(x.strip())
print("-------------")
#lower & UPPER 
y =  " Mustafa Mohamed "
print(y.lower())
print(y.upper())
print("-------------")
#///////////////////////////////////////
print(y.replace("M","A"))
print("-------------")
#///////////////////////////////////////
z = "mustafa ,mohamed"
print(z.split(","))
print(type(z.split(",")))   #type is list
print("-------------") 
#////////////////////////////////////
text = "today is too rainy "
b = "day" in text
print(b)                  #out is boolian
print("-------------") 
#join() : see output/////////////////
m = ["I","am","student"]
print(" not ".join(m))
print("-------------") 
#multiply string////////////////////////
n = 3 
print(x*n)
print("-------------") 
#find /////////////////////////////////
text = "today is too rainy "
print(text.find("too"))    #out is index
print(text.find("too",3,12))    #out is index
print("-------------") 
#count() counts time of iterations 
text = "rainy !,today is too rainy "
print(text.count("rainy"))
print("-------------") 
#isnumeric()///////////////////////////
r = "15485"
print(r.isnumeric())    #bool
print("-------------") 
#substitution/////////////////////////
v = 5
print(f"can i ask you {v} questions ")
print("can i ask you "+str(v)+" questions ")
print("can i ask you {} questions ".format(v))
print("can i ask you %d questions " %v)
print("-------------") 
#raw string //////////////////////////////
print(r"hellow\nworld")         #nothing happens
print("hellow\nworld")     #\n here is new line 
