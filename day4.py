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


    






 
    





