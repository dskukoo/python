#day3

'''example = input("enter a number")
print("you entered", example)*/'''

'''data = input("Enter values").split(',')
print("you entered", data)'''

'''data = []

data.append(int(input("enter a number")))
data.append(input("enter a name"))
print("you entered", data)'''

mylist = []
mylist.append(int(input("enter a number")))
mylist.append(int(input("enter a number")))
''''sum = sum(mylist)
print("the sum is", sum)
'''
if mylist[0]%2==0 and mylist[1]%2==0:
    print("both are even")
elif mylist[0]%2!=0 and mylist[1]%2!=0:
    print("both are odd")

elif mylist[0]%2!=0 and mylist[1]%2==0:
    print(mylist[0], "is odd and", mylist[1], "is even")
else :
    print(mylist[0], "is even and", mylist[1], "is odd")

    

