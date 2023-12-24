#use a dictionary with ascii codes to replace 83 (S) with 80 (p)
mydict = {83: 80}
txt = "hello Sami"
print(txt.translate(mydict))
print("----------------")
#join :elements of an iterable into string
myTuple = ("mustafa","mohamed","ahmed")
d = "#".join(myTuple)
print(d)    #    ..replace (,) with  (#)
print("----------------")
#format()///////////////////////
txt = "for only {price: .3f} dollars!"   #.3f num of zeros after 49.000
print(txt.format(price = 49))
print("----------------")
#encode //////////////////////////
txt = "my name is 𝓢𝓗𝓜𝓢𝓐𝓛'𝓐𝓢𝓨𝓛"
x = txt.encode()
print(x)
print("----------------")
#endswitch / check if string ends with punctuation sign (.or any sign)
txt = "hello, i am here :"
print(txt.endswith(":"))
print("----------------")
#title() :coverts first character of each word to upper case
print(txt.title())
print("----------------")
