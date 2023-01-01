
# Exercises: Level 1
## 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

"""Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""

my_age = input("Enter your age: ")
x = 18 - int(my_age)
if int(my_age) >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need',end = ' ' ) 
    print(x,end = ' ') 
    print('more years to learn to drive.')


## 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

"""Enter your age: 30
You are 5 years older than me.
"""
your_age = input("Enter your age: ")
my_age = input("Enter my age: ")
x = (int(your_age) - int(my_age))
if int(x)>0:
    if int(x)==1:
        print('You are',end = ' ')
        print(x,end = ' ')
        print('year older than me')
    else:
        print('You are',end = ' ')
        print(x,end = ' ')
        print('years older than me')
elif int(x) == 0:
    print('You are same age as me')

elif int(x)==-1:
    print('You are',end = ' ')
    print(abs(x),end = ' ')
    print('year younger than me')
        
else:
    print('You are',end = ' ')
    print(abs(x),end = ' ')
    print('years younger than me')

3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3

a = input("Enter number one: ")
b = input("Enter number two: ")

if a > b:
    print (a,end = ' ')
    print ('is greater than',end = ' ')
    print (b)
    
elif a < b:
    print (a,end = ' ')
    print ('is less than',end = ' ')
    print (b)
    
else:
    print (a,end = ' ')
    print ('is equal to',end = ' ')
    print (b)
    
# Exercises: Level 2

1. Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

scores = input("Enter your scores: ")
if 80<int(scores)<100:
    print('A')
elif 70<int(scores)<79:
    print('B')
elif 60<int(scores)<69:
    print('C')
elif 50<int(scores)<59:
    print('D')
elif 0<int(scores)<49:
    print('F')
else:
    print('E')

2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season = input("Enter the month here: ")

if season == 'September' or season == 'October' or season == 'November':
    print('Autumn')
elif season == 'December' or season == 'January' or season == 'February':
    print('Winter')
elif season == 'March' or season == 'April' or season == 'May':
    print('Spring')
elif season == 'June' or season == 'July' or season == 'August':
    print('Summer')   

3. The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

x = input("Enter the fruit name here: ")
fruits = ['banana', 'orange', 'mango', 'lemon']
if x in fruits:
    print('That fruit already exist in the list')
else:
   fruits.insert(0,x)
   print(fruits)

# Exercises: Level 3
Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

 person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    print((person['skills'])[2])

 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 
 person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'Python'in person['skills']:

    print (person['skills'])
 
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 
 person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print (person['skills'])


if 'JavaScript' and 'React' in person['skills']:
    print ('He is a front end developer')
elif 'Node'and 'Python'and 'MongoDB' in person['skills']:
    print ('He is a backend developer')        
elif 'React'and 'Node'and 'MongoDB' in person['skills']:
    print ('He is a fullstack developer')
else:
    print('unknown title')  
 
 * If the person is married and if he lives in Finland, print the information in the following format:
 
 Asabeneh Yetayeh lives in Finland. He is married.
 
 person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
   }
}

if person['is_marred']== True and person['country'] == 'Finland' :
        
        print ('Asabeneh Yetayeh lives in Finland. He is married.')