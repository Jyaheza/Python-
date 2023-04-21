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
#tuples 
tuple1=("one",) # add the comma for python to consider is a tuple not a string 
tuple2=("one",2,"Three",4.0,False) # to change elements of a turple turn it into a list change it same adding items amd removing
listtuple=list(tuple1)
listtuple[0]=("rimwe")
tuple1=tuple(listtuple) 
tuple2+=tuple1 # adding a tuple to another is possible 
(var1,var2,*list)=tuple2 # unpacking a tuple, the first two goes into vars and the remaining makes list in the last with *
tuple2=tuple1*2 #doubling the tuple 
print(tuple2)

# Sets Unchengeable, unordered, Dont allow duplicates 
thisSet={"money", "Family", "career", "Health", "happiness"}
print(thisSet)
print(thisSet)
# we cant change elements of set but we can add
thisSet.add(True)
thisSet.update(set("More")) # you can an any iterable using update 
print(thisSet)
thisSet.remove("career")
print(thisSet)
print(thisSet.pop()) # removes a random item
set2={"more","money","more","Problems"}
set3= thisSet.union(set2)# returns a new set with alll elements included both update and union excludes duplicates 
thisSet.intersection_update(set2) # keeps items that are same in the other set only 
print(thisSet) 
set3.symmetric_difference_update(set2) # keeps all but the duplicates

# Dictionaries 

thisDictionary= {
    "Name": "Maurice Irakoze Jyaheza",
    "Date of Birth": " 10 feb 2001",
    "Major": " CS "
}
print(thisDictionary["Name"])
print(thisDictionary.get("Major"))
listOfKeys=thisDictionary.keys()# gets keys only 
thisDictionary["other"]= "likes food"
listofValues=thisDictionary.values()#gets values 
print(thisDictionary.items()) # returns all the items as turples in a list 
if "Name" in thisDictionary:
    print("The dictionanary has a name")
thisDictionary.update({"Name": "Mo"})
print(thisDictionary.get("Name"))
thisDictionary.pop("other") # or del thisDictionary("other")
#functions finished all of it but lost the code 

