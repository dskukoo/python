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

'''n = int(input("enter a number"))
sum=0
i=1
while n>=i:
    

    sum+=i
    i+=1
print("the sum is", sum)'''

#day6

'''n = int(input("enter a number"))
i=1
while i<=10:
    print(n,"X",i,"=",n*i)
    i+=1'''
#day 7 
'''count=0
a = int(input("enter a number"))
while a>0:
    a=a//10
    count+=1
print("the number of digits is", count)'''

"""a = int(input("enter a number"))
reverse = 0
while a>0:
    digit = a%10
    reverse = reverse*10 + digit
    a = a//10
print("the reverse is", reverse)"""

'''word = input("enter a word")
is_palindrome = True

for i in range (len(word)//2):

    if word[i] != word[-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")'''

'''reverse=''
word = input("Enter a word")
vowels= 'aeiouAEIOU'
count = 0

for char in word:
    if char in vowels:
        count=count+1
print("the number of vowel in ",word," is ",count)        

for i in range(len(word)):
    reverse = reverse + word[-i-1]

print(reverse)'''

'''number = int(input("Enter a word"))
orignal = number

reverse = 0
while number > 0:
    digit = number%10
    reverse = reverse*10 + digit
    number=number//10

if reverse==orignal:
    print("it is pallindrome")

else:
    print("its not pallindrome")'''
'''
ls =[]
i=0
j=0
largest = 0
for i in range(5):
    number = int(input("enter a number"))
    ls.append(number)
    i=i+1

for j in range(5):
    if ls[j]>largest:
        largest=ls[j]
        j=j+1
    
print(largest)'''

'''ls = [1,2,3,4,5,]
sum=0
for num in ls:
    sum=sum+num
print(sum)'''


'''my_list = [1,2,3,4,4,5]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)'''

'''my_list = [1,2,3,4,5] 
largest = 0
s_largest = 0 
for num in my_list:
    if num>largest:
       largest=num
for num in my_list:
    if largest>num>s_largest:
        s_largest=num
print(s_largest)'''


'''word1=input("enter a word")
word2= input("Enter a 2nd word")
target = 'aeiouAEIOU'

def Volwels(word):
    count=0
    for char in word:
        if char in target:
            count=count+1
    print(word,"has",count,"volwels")
        
Volwels(word1)
Volwels(word2)'''



'''a= int(input("enter a nuumber"))
b=int(input("enter a nuumber"))

def addition(a,b):
    print(a+b)
addition(a,b)'''

'''num=int(input("enter a number"))

def Factorial(num):
    factorial=1
    i=1
    for i in range(1,num+1):
        factorial=factorial*i
        i+=1
    print(factorial)

Factorial(num)'''

#import random

'''
a=int(input("enter"))

def num(a):
    if a%3==0 or a%5==0 or a%7==0:
        print(a, "is a odd num")
    else:
        print(a,"is even number")
num(a)'''

'''a= random.randint(1,10)

b=int(input("Enter your gusse"))

if a==b:
    print("you gussed it right")
    
else:
    print("wrong")'''

#  menu based calculator 

'''operation = int(input("What operation you want to perform\n"
"1.Addition\n" \
"2.substraction\n" \
"3.multiply\n" \
"4.divide\n"))

def add(a,b):
    print(a+b)

def substract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a//b)

if operation==1:
    a=float(input("enter 1st "))
    b=float(input("enter 2nd "))
    add(a,b)

elif operation==2:
    a=float(input("enter 1st "))
    b=float(input("enter 2nd "))
    substract(a,b)

elif operation==3:
    a=float(input("enter 1st "))
    b=float(input("enter 2nd "))
    multiply(a,b)

elif operation==4:
    
    a=float(input("enter 1st "))
    b=float(input("enter 2nd "))
    if b==0:

        print("invail")
    else:
        divide(a,b)

else:
    print("invaild")'''



'''class_marks=[ ]
stu= int(input("How many student is in class"))
i=0
for i in range(stu):
    marks=int(input(f"Enter Marks of roll no {i+1}"))
    class_marks.append(marks)
    i+=1

def calculate(a):
    percentage=a/600*100
    return percentage

def grade(a):
    if a>=80:
        return 'A'
    elif a>=60:
        return 'B'
    elif a>=40:
        return 'C'
    elif a>=33:
        return 'D'
    else:
        return "failed"

for num in class_marks:
    per=calculate(num)
    g=grade(num)
    print("The percentage of student is ",per,"and the grade is", g)'''
task=[]
ls='False'
def operations(op):                      
        if op==1:
            new_task=input("Enter your Task")
            task.append(new_task)
            query = input("do you want to add another task[y/n]?")
            while query!="n":
                n_task=input("Enter your Task")
                task.append(n_task)
                query = input("do you want to add another task[y/n]?")
        elif op==2:
            i=0
            for i in range(len(task)):
                print(i+1," ",task[i])
                i+=1              
        elif op==3:
            
            for i in range(len(task)):
                print(i+1," ",task[i])
                i+=1
            d_task=int(input("Which Task do you want to delete"))
            task.pop(d_task-1)        
        elif op==4:
            return 'True'
                     
        else:
            print("Invaild")
        print(task)
while ls!='True':
    op=int(input("What operation do you want to perform\n\n1.Add task\n2.view task\n3.Delete task\n\n4.Exit"))
    ls=operations(op)
    

        




                     

    











    




















    






 
    





