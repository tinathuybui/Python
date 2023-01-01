a = 20
b = 10 
area = 0.5*a*b
print('area of the triangle : ',area)

a = 5
b = 4
c = 3
perimeter = a+b+c
print('perimeter of the triangle : ', perimeter)

x1 = 2
y1 = 2
x2 = 6
y2 = 10

m = y2-y1/x2-x1

print('Slope = ',m)

import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10

d = math.sqrt(((x1-y1)**2)+((x2-y2)**2))

print('Euclidean_distance =',d)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.?
    y  = (x**2) + (6*x) + 9
    print (x,y == 0)



#Find the length of 'python' and 'dragon' and make a falsy comparison statement
len('python')
len('dragon')
print(len('dragon')>len('python'))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on in python', 'on' in 'python')
print('on in dragon', 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence

print('jardon' in 'I hope this course is not full of jargon')

#There is no 'on' in both dragon and python
print ('on' not in 'python' and 'on' not in 'dragon')

#Find the length of the text python and convert the value to float and convert it to string
float(len('python'))
str(6.0)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

a = 78
if (a%2) == 0:
  print("a is an even number")
else:
  print("a is not an odd number")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print ('7//3' == int(2.7))

#Check if type of '10' is equal to type of 10
print (type('10') == type(10))

#Check if int('9.8') is equal to 10
print (int(9.8) == 10)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120

a=40
b=28
hours = a
rate_per_hour = b
print('Your weekly earning is', a*b)


#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.

a = 100 
number_of_years_you_have_lived = a
print('You have lived for' ,a*365*24*60*60, 'seconds')

#Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

for a in range(1,6):
  print(a,a**0,a**1,a**2,a**3)

