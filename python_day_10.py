
# Exercises: Level 1

##1. Iterate 0 to 10 using for loop, do the same using while loop.

### for loop
for number in range(11):
    print(number) 
    
### while loop
count = 0
while count < 11:
    print(count)
    count = count + 1


##2. Iterate 10 to 0 using for loop, do the same using while loop.

### for loop
for number in range(10,-1,-1):
    print(number) 
    
### while loop 
count = 10
while count < 11:
    print(count)
    count = count - 1 
    if count == -1:
        break

##3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
  
a = ['#', '##','###','####','#####', '######','#######']
for b in a:
    print(b)

### While loop
    
n=7
i=1;j=0
while(i<=n):
    while(j<=i-1):
        print("#",end="")
        j+=1
    print("\r")
    j=0;i+=1

### for loop 
n = 8
for i in range(n):
    # nested loop
    for j in range(i):
        # display number
        print('#',end ="")
    # new line after each row
    print('')

##4. Use nested loops to create the following:

### for loop  
n = 8
for i in range(n):
    for i in range(n):
        print('#', end = '  ')
    print()
    
### while loop

n = 8
i = 0
while(i < n):
    j = 0
    while(j < n):      
        j = j + 1
        print('#', end = '  ')
    i = i + 1
    print('')


# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #



##5. Print the following pattern:
    
n = 11
for i in range(n):
    for i in range(n):
        print(i,'x',i,'=',i*i)
    print()

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

##6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

n = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in n:
    print(i)

##7. Use for loop to iterate from 0 to 100 and print only even numbers

n = 101
for i in range(n):
    if i%2==0:
        print(i)
        
    
##8. Use for loop to iterate from 0 to 100 and print only odd numbers

n = 101
for i in range(n):
    if i%2>0:
        print(i)

# Exercises: Level 2
##1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
###The sum of all numbers is 5050.

sum = 0
for i in range(0, 101):
    sum = sum + i

print('The sum of all numbers is', sum)
    
##2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

###The sum of all evens is 2550. And the sum of all odds is 2500.

sum = 0
for i in range(0, 101):
    if i%2==0:
        sum = sum + i
print('The sum of all evens is',sum)
            
sum = 0
for i in range(0, 101):
    if i%2>0:
        sum = sum + i
print('The sum of all odds is',sum)

# Exercises: Level 3
##1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

newlist = [x for x in countries if "land" in x]
print (newlist)

##2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruit = ['banana', 'orange', 'mango', 'lemon']
reversed_list = []
for value in fruit:
  reversed_list = [value] + reversed_list
  
print("List after reverse : ", reversed_list)
##3. Go to the data folder and use the countries_data.py (called it y) file.

###- What are the total number of languages in the data
lang_set = set()
for x in y:
    for lang in x['languages']:
        lang_set.add(lang)
print (len(lang_set))

###- Find the ten most spoken languages from the data
###- Find the 10 most populated countries in the world

