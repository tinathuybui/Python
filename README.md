
# Python

Day 1:

- Commmand to check python version 

python --version

<img width="888" alt="Screen Shot 2022-08-22 at 9 43 38 pm" src="https://user-images.githubusercontent.com/89682120/185913499-4ffe53ff-eb1f-4dbe-be89-a6b48305519b.png">

- To start type python and enter python scripts after >>>
- To exist type exit() after >>> and click Enter

<img width="886" alt="Screen Shot 2022-08-22 at 9 47 48 pm" src="https://user-images.githubusercontent.com/89682120/185914325-9f32ef98-9b8f-4c48-a9f0-053127b9e534.png">

Noted: use * to represent multiply in python not x
       ** is the exponential operator. Eg 3**2 = 3^2 = 3*3

- to start a comment in python use #. For multiple comments, write them in between two triple quotes set """
- python file has an extension .py
- different data types in python:
1. Number
a. Integer: Round numbers
b. Float: numbers with decimala

2. String 
3. Boolean: True or False data
4. List: used to store multiple items in a single variable. List items are ordered, changeable, and allow duplicate values.

Example:

```
>>> thislist = ["apple", "banana", "cherry", "apple", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry', 'apple', 'cherry']
```
5. Dictionary: an unordered collection of data in a key value pair format.

Example:

```
>>> thisdict = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>>
```
6. Tuple: similar like list but cannot modified once it has been created. Tutples are written with round brackets.

Example:

```
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>>
```
7. Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Example: duplicate value will be ignored. 
```
>>> thisset = {"apple", "banana", "cherry", "apple"}
>>> print(thisset)
{'cherry', 'banana', 'apple'}
```
- use type () command to check data types:

```>>> type ((1,2,4,10))
<class 'tuple'>
```
Day 2:

- List of python build-in function:

https://docs.python.org/3.9/library/functions.html


- Variables are containers for storing data values. 

- Python Variable Rules:

1. must start with a letter or underscore character
2. cannot start with a number
3. can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. case-sensitive 

- Example of valid variable name:
firstname
last_name

- Example of invalid variable name:
first-name
last-name

- Casting is converting one data type to another data type:

- Example convert string to interger and string to float:

```
>>> number_string=234.56
>>> print('number_integer',int(number_string))
number_integer 234
```
```
>>> print('number_float', float(number_string))
number_float 234.56
```
Day 3:

- Boolean represents one of two values: True and False with the first letter should be capital.
- Different types of opperators:
Link to examples of different typea of operators:
https://www.w3schools.com/python/python_operators.asp

1. Assignment operators:

They are used to assign values to variables. 

2. Arithmetic operators:

They are used with numberic values to perform commmon mathematical operators.

Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b

3. Comparasion operators:

They are used to compare two values and check if a value is greater or less or equal to other value.

4. Logical operators:

They are used to combine conditional statement. Key words are and, or and not.

Day 4:

- Strings are any data type written as a text. Strings are surrounded by single, double or triple quotes. 

- String Concatenation is merging strings together.

Eg:
```
>>> first_name='Tina'
>>> last_name='Bui'
>>> full_name=first_name + ' ' +last_name
>>> print(full_name)
```
- Escape sequences:  \ followed by a character is an escape sequence.

\n: new line

\t: Tab means(8 spaces)

\\: Back slash

\': Single quote (')

\": Double quote (")


Eg:

print('How are you?\nAnd you ?')

- String format:

Old Style String Formatting (% Operator):
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

Eg:
```
base = 2
height = 4 
area = 1/2 * base * height
formated_string = 'The area of triangle with base = %d and height = %d is %d.' %(base, height, area)
print(formated_string)
```

New Style String Formatting (str.format)(python version 3)
Eg:

```
base = 2
height = 4 
area = 1/2 * base * height
formated_string = 'The area of triangle with base = {} and height = {} is {}'.format(base, height, area)
print(formated_string)
```

String Interpolation / f-Strings (Python 3.6+)

String start with f - f.string and data can be injected in their corresponding position.

Eg:
```
a = 2
b = 4
print(f'1/2 * {a} * {b} = {1/2*a*b}')
```
- Python Strings as Sequences of Characters

Unpacking Characters

```
name = 'Tina_Bui'
a,b,c,d,e,f,g,h = name#
print(a)
print(b) 
print(c) 
print(d) 
print(e)
print(f) 
print(g) 
print(h)
```
Accessing Characters in Strings by Index
In Python counting starts from 0, the first letter of the string is 0 and the last letter of the string is the length of the string - 1

```
name = 'Tina_Bui'
first_letter = name [0]
print(first_letter)
last_letter = name[-1]
print(last_letter)
```

Slicing Python Strings

Slice string into substring 


```
name = 'Tina_Bui'
first_three = name [0:3]
print(first_three)
last_three = name[5:8]
print(last_three)
# Another way
last_three = name[-3:]
print(last_three)
```

Reverse a string
```
name = 'Tina_Bui'
print(name[::-1])

```
Skipping Characters While Slicing
```
a_string[start:stop:step]
```

```
name = 'Tina_Bui'
Ta = name[0:5:3] 
print(Ta)
```
- String methods

Below are example of string methods help to format strings

capitalize(): Converts the first character of the string to capital letter





