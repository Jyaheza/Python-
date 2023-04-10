#python variables are cool
from tokenize import Double

#intro
x="Hello Word"
y=str(4)
z=float(4)
m=int(4)
print(y)
print(z)
print(m)
print(x+" is concatenated with "+y)
if 5>4:
    print(x)
    print("error")
else:
    print("5<4")
names={"Maurice",'Fabiola',21}
name1,name2,age=names
print(name1)
print(name2)
print(age)
#data types
a=10 #int 
b=10.6 #float
print(a*b)
c= " a number " #str
d= 1j #complex
e= ["one","two",3] #list
f={"one",2,"Three"} #set
g= (1,"two","three") # turple
h={"name":"mo","age":1} # dict
i= frozenset({"one",2,"three"}) #frozenset
j=range(10) #range 
k=True #bool

#strings

longString='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua''' 
print(longString)
print(longString[0]) # prints L
print(len(longString)) # lenghth of string
for l in "Maurice":
    print(l) #prints every letter in my name 
print("tempor" in longString) # prints true if tempor is in and false if not 
if "elit" not in longString:
    print("Not in")
else:
    print("in")
   #slicing
exampleString=(" God is Good! All the Time ")
print(exampleString[2:4]) #prints characters from position 2 to 4(not included) of the text 
print(exampleString[:5]) # all characters in front of one at position 5( not included)
print(exampleString[5:]) # prints all characters after one  at position 5( included)
print(exampleString[-5:-2]) # prints characters from 5 staring from the right to the 2 from the right( indexes start from 1)
print(exampleString.upper) # uppercase 
print(exampleString.lower) # lowercase
print(exampleString.strip) # removes white spaces on beginning and end 
print(exampleString.split(" ")) # splits the sentence with delimiter " "
print(exampleString.replace("All","Every")) # replaces All with Every
formatString= " My name is {} and I am {} years old. I like {}"
print(formatString.format("Maurice",19,"to play basketball"))

#collections 

  # list 
thisList=['one',2,'three','one',False]
print(len(thisList))
print(thisList[-1]) #last item 
if "one" in thisList:
    print("one")
thisList.insert(2,"temp")
print(thisList)
thisList.append(True)
thisList.extend(e)
print(thisList) #adds any iterable
thisList.remove("one")
thisList.pop(1)
del thisList[2]
[print(elt) for elt in thisList] # another way 
 #newlist=[elt2 for elt2 in thisList if "e" in elt2] creates a new list from the old list wjere every elemnt has "e" in it 
# syntax =>  newlist = [expression for item in iterable if condition == True]
testList=input("test list")
print(testList)
#next is functions
