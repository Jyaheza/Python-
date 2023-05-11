# Enter your code here. Read input from STDIN. Print output to STDOUT
def maximize(arr,m):
    res=0
    for x in range(len(arr)):
        res=res+int((arr[x]))**2 
    return res%m
temp=input()
k=int(temp.split(" ")[0])
#print(k)
m=int(temp.split(" ")[1])
#print(m)
maxNums=[]
for i in range(k):
    temp=input()
    tempArr=temp.split(" ")[1:]
    maxNums.append(max(map(int,tempArr)))   
print(maximize(maxNums,m))

