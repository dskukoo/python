#day3

'''example = input("enter a number")
print("you entered", example)*/'''

'''data = input("Enter values").split(',')
print("you entered", data)'''

'''data = []

data.append(int(input("enter a number")))
data.append(input("enter a name"))
print("you entered", data)'''

'''mylist = []
mylist.append(int(input("enter a number")))
mylist.append(int(input("enter a number")))
sum = sum(mylist)
print("the sum is", sum)

if mylist[0]%2==0 and mylist[1]%2==0:
    print("both are even")
elif mylist[0]%2!=0 and mylist[1]%2!=0:
    print("both are odd")

elif mylist[0]%2!=0 and mylist[1]%2==0:
    print(mylist[0], "is odd and", mylist[1], "is even")
else :
    print(mylist[0], "is even and", mylist[1], "is odd")

if mylist[0]>mylist[1]:
    print(mylist[0], "is greater than", mylist[1])

elif mylist[0]<mylist[1]:
    print(mylist[1], "is greater than", mylist[0])
else:
    print("both are equal")'''

'''mylist = []
a = int(input("enter a number"))
b = int(input("enter a number"))
mylist.append(a)
mylist.append(b)
operation = input("enter an operation")
if operation == '+':
    print("the sum is ",a+b)
elif operation == '-':
    print("the difference is ",a-b)

elif operation == '*' or operation == 'x' or operation == 'X':
    print("the product is ",a*b)

elif operation == '/' or operation == '÷':
    if b!=0:
        print("the quotient is ",a/b)
    else:
        print("division by zero is not allowed")'''
#day4

'''for i in range(0,50):
    if i%2!=0:
        print(i)'''

'''i = 60 
while i<50:
    print(i)
    i=i+1'''

    #day5

n = int(input("enter a number"))
sum=0
i=1
while n>=i:
    

    sum+=i
    i+=1
print("the sum is", sum)

    

