#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
a='Thirty'
b='Days'
c='Of'
d='Python'
e=a+ " "+b+ " " +c+ " " +d
print(e)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a='Coding'
b='For'
c='All'
string =a+" "+b+" "+c
print(string)

#Declare a variable named company and assign it to an initial value "Coding For All"

company='Coding For All'

#Print the variable company using print()
company='Coding For All'
print(company)

#Print the length of the company string using len() method and print()
len(company)

#Change all the characters to uppercase letters using upper() method
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Cut(slice) out the first word of Coding For All string
print(company[6:14])

#Check if Coding For All string contains a word Coding using the method index, find or other methods
print(company.index("Coding"))
print(company.find("Coding"))
print( 'Coding' in 'Coding For All')

#Replace the word coding in the string 'Coding For All' to Python
print(company.replace("Coding", "Python"))

#Change Python for Everyone to Python for All using the replace method or other methods
string = 'Python for Everyone'
print(string.replace("Everyone", "All"))

#Split the string 'Coding For All' using space as the separator (split())
print(company.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(","))

#What is the character at index 0 in the string Coding For All
print(company[0])

#What is the last index of the string Coding For All.
print(len(company) - 1)

#What character is at index 10 in "Coding For All" string
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'
x = 'Python For Everyone'
y = x.split()
for x in y:
    print(x [0], end="")

#Create an acronym or an abbreviation for the name 'Coding For All'.
company = 'Coding For All'
x = company.split()
for company in x:
    print(company [0], end="")
    
#Use index to determine the position of the first occurrence of C in Coding For All.
#The index() method only returns the first occurrence of the value.
company = 'Coding For All'
x = company.index("C")
print(x)

#Use index to determine the position of the first occurrence of F in Coding For All.
x = company.index("F")
print(x)
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding for All People'
x = string.rfind("l")
print(x)

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
x = string.index("because")
print(x)

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

string = 'You cannot end a sentence with because because because is a conjunction'
x = string.rindex("because")
print(x)

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
phrase = string[31:54]
print(phrase)

#Does 'Coding For All' start with a substring Coding?
string = 'Coding For All'
x = string.startswith("Coding")
print(x)

#Does 'Coding For All' end with a substring coding?
string = 'Coding For All'
x = string.endswith("Coding")
print(x)

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
x = string.lstrip()
print(x)

#Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python

string_1 = '30DaysOfPython'
string_2= 'thirty_days_of_python'
x = string_1.isidentifier()
y = string_2.isidentifier()
print(x,y)

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ("Django", "Flask", "Bottle", "Pyramid", "Falcon")

x = "#".join(list)

print(x)

#Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.

print('I am enjoying this challenge.\nI just wonder what is next.')

#Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki

print('Name      Age\tCountry\t City')
print('Asabeneh  250\tFinland\t Helsinki')

#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square

radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with radius %d is %d meters square' %(radius,area)
print(formated_string)

#Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
