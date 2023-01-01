Table of Contents
=================

* [Table of Contents](#table-of-contents)
* [Day 1:](#day-1)
   * [Commmand to check python version](#commmand-to-check-python-version)
   * [Different data types in python:](#different-data-types-in-python)
      * [1. Number](#1-number)
      * [2. String](#2-string)
      * [3. Boolean: True or False data](#3-boolean-true-or-false-data)
      * [4. List: used to store multiple items in a single variable. List items are ordered, changeable, and allow duplicate values.](#4-list-used-to-store-multiple-items-in-a-single-variable-list-items-are-ordered-changeable-and-allow-duplicate-values)
      * [5. Dictionary: an unordered collection of data in a key value pair format.](#5-dictionary-an-unordered-collection-of-data-in-a-key-value-pair-format)
      * [6. Tuple: similar like list but cannot modified once it has been created. Tutples are written with round brackets.](#6-tuple-similar-like-list-but-cannot-modified-once-it-has-been-created-tutples-are-written-with-round-brackets)
      * [7. Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.](#7-set-is-a-collection-which-is-unordered-unchangeable-and-unindexed-no-duplicate-members)
* [Day 2:](#day-2)
   * [List of python build-in function:](#list-of-python-build-in-function)
   * [Variables are containers for storing data values.](#variables-are-containers-for-storing-data-values)
   * [Python Variable Rules:](#python-variable-rules)
   * [Example of valid variable name:](#example-of-valid-variable-name)
   * [Example of invalid variable name:](#example-of-invalid-variable-name)
   * [Casting is converting one data type to another data type:](#casting-is-converting-one-data-type-to-another-data-type)
   * [Example convert string to interger and string to float:](#example-convert-string-to-interger-and-string-to-float)
* [Day 3:](#day-3)
   * [Boolean represents one of two values: True and False with the first letter should be capital.](#boolean-represents-one-of-two-values-true-and-false-with-the-first-letter-should-be-capital)
   * [Different types of opperators:](#different-types-of-opperators)
      * [1. Assignment operators:](#1-assignment-operators)
      * [2. Arithmetic operators:](#2-arithmetic-operators)
      * [3. Comparasion operators:](#3-comparasion-operators)
      * [4. Logical operators:](#4-logical-operators)
* [Day 4:](#day-4)
   * [Strings are any data type written as a text. Strings are surrounded by single, double or triple quotes.](#strings-are-any-data-type-written-as-a-text-strings-are-surrounded-by-single-double-or-triple-quotes)
   * [String Concatenation is merging strings together.](#string-concatenation-is-merging-strings-together)
   * [Escape sequences:  \ followed by a character is an escape sequence.](#escape-sequences---followed-by-a-character-is-an-escape-sequence)
   * [String format:](#string-format)
      * [Old Style String Formatting (% Operator):](#old-style-string-formatting--operator)
      * [New Style String Formatting (str.format)(python version 3)](#new-style-string-formatting-strformatpython-version-3)
      * [String Interpolation / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
   * [Python Strings as Sequences of Characters](#python-strings-as-sequences-of-characters)
      * [Unpacking Characters](#unpacking-characters)
      * [Accessing Characters in Strings by Index](#accessing-characters-in-strings-by-index)
   * [Slicing Python Strings](#slicing-python-strings)
      * [Slice string into substring](#slice-string-into-substring)
      * [Reverse a string](#reverse-a-string)
      * [Skipping Characters While Slicing](#skipping-characters-while-slicing)
   * [Different string methods](#different-string-methods)
* [Day 5:](#day-5)
   * [There are 4 buil-in data types in Python used to stored data namely: list, tuple. set, dictionary.](#there-are-4-buil-in-data-types-in-python-used-to-stored-data-namely-list-tuple-set-dictionary)
      * [List:](#list)
      * [Tutple](#tutple)
      * [Set](#set)
      * [Dictionary:](#dictionary)
   * [How to creat list:](#how-to-creat-list)
      * [Using list built-in function](#using-list-built-in-function)
      * [created using square brackets:](#created-using-square-brackets)
      * [Lists can have items of different data types](#lists-can-have-items-of-different-data-types)
      * [Accessing List Items Using Positive Indexing](#accessing-list-items-using-positive-indexing)
      * [Accessing List Items Using Negative Indexing](#accessing-list-items-using-negative-indexing)
   * [Unpacking List Items](#unpacking-list-items)
   * [Slicing Items from a List](#slicing-items-from-a-list)
   * [Modifying Lists](#modifying-lists)
   * [Checking Items in a List](#checking-items-in-a-list)
   * [Adding Items to a List](#adding-items-to-a-list)
   * [Inserting Items into a List](#inserting-items-into-a-list)
   * [Removing Items from a List](#removing-items-from-a-list)
      * [Removing Items Using Pop](#removing-items-using-pop)
      * [Removing Items Using Del](#removing-items-using-del)
   * [Clearing List Items](#clearing-list-items)
   * [Copying a List](#copying-a-list)
   * [Joining Lists](#joining-lists)
      * [Joining using extend() method](#joining-using-extend-method)
   * [Counting Items in a List](#counting-items-in-a-list)
   * [Finding Index of an Item](#finding-index-of-an-item)
   * [Reversing a List](#reversing-a-list)
   * [Sorting List Items](#sorting-list-items)
* [Day6:](#day6)
   * [Create a tuple](#create-a-tuple)
   * [Tuples length](#tuples-length)
   * [Accessing Tuple Items](#accessing-tuple-items)
   * [Slicing tuples](#slicing-tuples)
   * [Changing Tuple to a List](#changing-tuple-to-a-list)
   * [Checking an Item in a Tuple](#checking-an-item-in-a-tuple)
   * [Joining Tuples](#joining-tuples)
   * [Deleting Tuples](#deleting-tuples)
* [Day7:](#day7)
   * [Sets](#sets)
   * [A set is a collection](#a-set-is-a-collection)
* [A set is used to store multiple items in a single variable](#a-set-is-used-to-store-multiple-items-in-a-single-variable)
* [A set is written with curly brackets](#a-set-is-written-with-curly-brackets)
* [Create a set](#create-a-set)
   * [Creating a set with initial items](#creating-a-set-with-initial-items)
   * [Getting set'length](#getting-setlength)
   * [Checking an Item](#checking-an-item)
   * [Adding Items to a Set](#adding-items-to-a-set)
   * [Removing Items from a Set](#removing-items-from-a-set)
   * [Clearing Items in a Set](#clearing-items-in-a-set)
   * [Deleting a Set](#deleting-a-set)
   * [Converting List to Set](#converting-list-to-set)
   * [Joining Sets](#joining-sets)
   * [Checking Subset and Super Set](#checking-subset-and-super-set)
   * [Checking the Difference Between Two Sets](#checking-the-difference-between-two-sets)
* [The syntax returns the differences between two sets](#the-syntax-returns-the-differences-between-two-sets)
   * [Finding Symmetric Difference Between Two Sets](#finding-symmetric-difference-between-two-sets)
   * [Joining Sets](#joining-sets-1)
   * [check if two sets are joint or disjoint using isdisjoint() method.](#check-if-two-sets-are-joint-or-disjoint-using-isdisjoint-method)
* [Day8:](#day8)
   * [Dictionaries](#dictionaries)
   * [A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.](#a-dictionary-is-a-collection-of-unordered-modifiablemutable-paired-key-value-data-type)
   * [Creating a Dictionary](#creating-a-dictionary)
   * [Dictionary Length](#dictionary-length)
   * [Accessing Dictionary Items](#accessing-dictionary-items)
   * [Modifying Items in a Dictionary](#modifying-items-in-a-dictionary)
   * [Checking keys](#checking-keys)
   * [Removing Key and Value Pairs](#removing-key-and-value-pairs)
   * [change dictionary to a list of items](#change-dictionary-to-a-list-of-items)
   * [Clearing a Dictionary](#clearing-a-dictionary)
   * [Deleting a Dictionary](#deleting-a-dictionary)
   * [Copy a Dictionary](#copy-a-dictionary)
   * [Getting Dictionary Keys as a List](#getting-dictionary-keys-as-a-list)
   * [Getting Dictionary Values as a List](#getting-dictionary-values-as-a-list)
* [Day9:Conditionals](#day9conditionals)
   * [If condition](#if-condition)
   * [If Else](#if-else)
   * [If Elif Else](#if-elif-else)
   * [Shorthand If Else](#shorthand-if-else)
      * [Nested If](#nested-if)
   * [If condition and logical operators](#if-condition-and-logical-operators)
   * [If and Or](#if-and-or)
* [Day 10: Loops](#day-10-loops)
   * [While loop](#while-loop)
   * [Break and continute](#break-and-continute)
   * [For loop](#for-loop)
   * [Range function](#range-function)
   * [Nested for loop](#nested-for-loop)
   * [For Else](#for-else)
   * [Pass](#pass)
* [Day 11:](#day-11)
   * [Functions](#functions)
      * [Definition](#definition)
      * [Declaring and Calling a Function](#declaring-and-calling-a-function)
      * [Function without Parameters](#function-without-parameters)
      * [Use return function to return values](#use-return-function-to-return-values)
      * [Function with Parameters](#function-with-parameters)
      * [Passing Arguments with Key and Value](#passing-arguments-with-key-and-value)
      * [Function with Default Parameters](#function-with-default-parameters)
      * [Arbitrary Number of Arguments](#arbitrary-number-of-arguments)

# Day 1:

## Commmand to check python version 

python --version

<img width="888" alt="Screen Shot 2022-08-22 at 9 43 38 pm" src="https://user-images.githubusercontent.com/89682120/185913499-4ffe53ff-eb1f-4dbe-be89-a6b48305519b.png">

- To start type python and enter python scripts after >>>
- To exist type exit() after >>> and click Enter

<img width="886" alt="Screen Shot 2022-08-22 at 9 47 48 pm" src="https://user-images.githubusercontent.com/89682120/185914325-9f32ef98-9b8f-4c48-a9f0-053127b9e534.png">

Noted: use * to represent multiply in python not x
       ** is the exponential operator. Eg 3**2 = 3^2 = 3*3

- to start a comment in python use #. For multiple comments, write them in between two triple quotes set """
- python file has an extension .py

##  Different data types in python:

### 1. Number
a. Integer: Round numbers
b. Float: numbers with decimala

### 2. String 
### 3. Boolean: True or False data
### 4. List: used to store multiple items in a single variable. List items are ordered, changeable, and allow duplicate values.

Example:

```py
>>> thislist = ["apple", "banana", "cherry", "apple", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry', 'apple', 'cherry']
```

### 5. Dictionary: an unordered collection of data in a key value pair format.

Example:

```py
>>> thisdict = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>>
```

### 6. Tuple: similar like list but cannot modified once it has been created. Tutples are written with round brackets.

Example:

```py
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>>
```

### 7. Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

Example: duplicate value will be ignored. 

```py
>>> thisset = {"apple", "banana", "cherry", "apple"}
>>> print(thisset)
{'cherry', 'banana', 'apple'}
```
- use type () command to check data types:

```py
>>> type ((1,2,4,10))
<class 'tuple'>
```

# Day 2:

## List of python build-in function:

https://docs.python.org/3.9/library/functions.html


## Variables are containers for storing data values. 

## Python Variable Rules:

1. must start with a letter or underscore character
2. cannot start with a number
3. can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. case-sensitive 

## Example of valid variable name:
firstname
last_name

## Example of invalid variable name:
first-name
last-name

## Casting is converting one data type to another data type:

## Example convert string to interger and string to float:

```py
>>> number_string=234.56
>>> print('number_integer',int(number_string))
number_integer 234
```

```py
>>> print('number_float', float(number_string))
number_float 234.56
```

# Day 3:

## Boolean represents one of two values: True and False with the first letter should be capital.
## Different types of opperators:
Link to examples of different typea of operators:
https://www.w3schools.com/python/python_operators.asp

### 1. Assignment operators:

They are used to assign values to variables. 

### 2. Arithmetic operators:

They are used with numberic values to perform commmon mathematical operators.

Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b

### 3. Comparasion operators:

They are used to compare two values and check if a value is greater or less or equal to other value.

### 4. Logical operators:

They are used to combine conditional statement. Key words are and, or and not.

# Day 4:

## Strings are any data type written as a text. Strings are surrounded by single, double or triple quotes. 

## String Concatenation is merging strings together.

Eg:

```py
>>> first_name='Tina'
>>> last_name='Bui'
>>> full_name=first_name + " " + last_name
>>> print(full_name)
```
## Escape sequences:  \ followed by a character is an escape sequence.

\n: new line

\t: Tab means(8 spaces)

\\: Back slash

\': Single quote (')

\": Double quote (")


Eg:

print('How are you?\nAnd you ?')

## String format:

### Old Style String Formatting (% Operator):
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

Eg:

```py
base = 2
height = 4 
area = 1/2 * base * height
formated_string = 'The area of triangle with base = %d and height = %d is %d.' %(base, height, area)
print(formated_string)
```

### New Style String Formatting (str.format)(python version 3)
Eg:

```py
base = 2
height = 4 
area = 1/2 * base * height
formated_string = 'The area of triangle with base = {} and height = {} is {}'.format(base, height, area)
print(formated_string)
```

### String Interpolation / f-Strings (Python 3.6+)

String start with f - f.string and data can be injected in their corresponding position.

Eg:

```py
a = 2
b = 4
print(f'1/2 * {a} * {b} = {1/2*a*b}')
```
## Python Strings as Sequences of Characters

### Unpacking Characters

```py
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
### Accessing Characters in Strings by Index
In Python counting starts from 0, the first letter of the string is 0 and the last letter of the string is the length of the string - 1

```py
name = 'Tina_Bui'
first_letter = name [0]
print(first_letter)
last_letter = name[-1]
print(last_letter)
```

## Slicing Python Strings

### Slice string into substring 


```py
name = 'Tina_Bui'
first_three = name [0:3]
print(first_three)
last_three = name[5:8]
print(last_three)
# Another way
last_three = name[-3:]
print(last_three)
```

### Reverse a string

```py
name = 'Tina_Bui'
print(name[::-1])
```

### Skipping Characters While Slicing

```py
a_string[start:stop:step]
```

```py
name = 'Tina_Bui'
Ta = name[0:5:3] 
print(Ta)
```

## Different string methods

https://www.w3schools.com/python/python_ref_string.asp

Note: by default default Python‘s print() function ends with a newline

To print on the same line use end = " "

Eg:

```py
company = 'Coding For All'
x = company.split()
for company in x:
    print(company [0], end="")
```

# Day 5:

## There are 4 buil-in data types in Python used to stored data namely: list, tuple. set, dictionary.

They are collection which are:

### List:
- ordered 
- changeable
- allows duplicate members
- can be empty or have different data type items
- indexed, the first item has index [0]

### Tutple
- ordered
- unchangeable or unmodifiable(imutable)
- allow duplicate members

### Set
- unordered
- un-indexed and unmodofiable
- allow new items to the set
- not alllow duplicate members

### Dictionary:
- unordered
- changeable(modifiable) and indexed
- not alllow duplicate members

## How to creat list:

### Using list built-in function
Eg:

```py
x = list(('chanel', 'gucci', 'dior'))

print(x)
```

### created using square brackets:

Eg:

```py
wish_list = ["chanel", "gucci", "dior"]
print(wish_list)
```

```py
list = [] # empty list
print(list)
```

### Lists can have items of different data types

```py
list = ["chanel", 5000, False, 1, "high_end"]

```

### Accessing List Items Using Positive Indexing

```py
wish_list = ["chanel", "gucci", "dior"]

first_item = wish_list[0]
```

### Accessing List Items Using Negative Indexing

-1 refers to the last item, -2 refers to the second last item

```py
wish_list = ["chanel", "gucci", "dior"]

second_item = wish_list[-2]
```

## Unpacking List Items

If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

+ First, unpack the needed elements to variables.
+ Second, pack the leftover elements into a new list and assign it to another variable.
By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable. 

Eg:

```py
colors = ['red', 'blue', 'green']
red, blue, *other = colors

print(red)
print(blue)
print(other)
```

Output:

```py
red
blue
['green']
```

https://www.pythontutorial.net/python-basics/python-unpack-list/

## Slicing Items from a List
We can specify a range of indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
Eg:

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
full_wish_list = wish_list[0:4] # it returns all values
# this will also give the same result as the one above
full_wish_list = wish_list[0:] # if we don't set where to stop it takes all the rest
gucci_dior = wish_list[1:3] # it does not include the first index
gucci_dior_ysl = wish_list[1:]
gucci_ysl = wish_list[::2] # here we used a 3rd argument, step. It will take every 2cnd item
```

## Modifying Lists

Eg:

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
wish_list[0] = 'zara'
print(wish_list)       #  ['zara', 'gucci', 'dior','ysl']
last_index = len(wish_list - 1
wish_list[last_index] = 'aje'
print(fwish_list)        #  ['chanel', 'gucci', 'dior', 'aje']
```
## Checking Items in a List

Eg:

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
does_exist = 'channel' in wish_list
print(does_exist)  # True
does_exist = 'zara' in wish_list
print(does_exist)  # False
```

## Adding Items to a List

```py
# syntax
lst = list()
lst.append(item) #To add item to the end of an existing list
```

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
wish_list.append('zara')
print(wish_list)  #['chanel', 'gucci', 'dior', 'ysl','zara']
```

## Inserting Items into a List

```py
# syntax # use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
wish_list.insert(2, 'zara') 
print(wish_list)           # ['chanel', 'gucci', 'zara', 'dior', 'ysl']
```

## Removing Items from a List

```py
# syntax 
lst = ['item1', 'item2']
lst.remove(item)
```
### Removing Items Using Pop

```py
# syntax# pop() method removes the specified index, (or the last item if index is not specified)
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

Eg:

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
wish_list.pop()
print(wish_list       # ['chanel', 'gucci', 'dior']
```

### Removing Items Using Del

```py
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```

Eg:

```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
del wish_list[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(wish_list)       # ['chanel', 'ysl']
```

## Clearing List Items

```py
# syntax #empties the list
lst = ['item1', 'item2']
lst.clear()
```

Eg:


```py
wish_list = ["chanel", "gucci", "dior", "ysl"]
wish_list.clear()
print(wish_list)  #[]
```

## Copying a List

```py
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

lst_copy is a reference of lst, any changes make in lst_copy  will also modify the original.

## Joining Lists

```py
Plus Operator (+)
# syntax
list3 = list1 + list2
```

### Joining using extend() method

```py
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

##  Counting Items in a List

```py
# syntax #count() method returns the number of times an item appears in a list
lst = ['item1', 'item2']
lst.count(item)
```

## Finding Index of an Item

```py
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

## Reversing a List

```py
# syntax
lst = ['item1', 'item2']
lst.reverse()
```

## Sorting List Items

sort(): this method modifies the original list  in ascending order

```py
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

`sorted()`: returns the ordered list without modifying the original list

# Day6:
Tuples is a collection which is ordered and unchangeable.
Tuples are written with round bracket.

## Create a tuple
- empty tuple

```py
empty_tuple = ()
```
- tuple with initial values

```py
# syntax
tpl = ('item1', 'item2','item3')
```
## Tuples length

```py
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```
## Accessing Tuple Items
- Positive Indexing
```py 
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```
- Negative Indexing: -1 refer to the last item

```py 
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```
## Slicing tuples

- Range of Positive Indexes
```py 
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
``` 
- Range of Negative Indexes

```py 
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
```
## Changing Tuple to a List

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```
## Checking an Item in a Tuple

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```
## Joining Tuples

```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```
## Deleting Tuples

```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

# Day7:
## Sets
## A set is a collection
- unordered
- unchangeable ( but can remove and add new items)
- unindexed
# A set is used to store multiple items in a single variable
# A set is written with curly brackets
# Create a set

```py
# syntax
st = {}
# or
st = set()
```

## Creating a set with initial items

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```
## Getting set'length

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```
## Checking an Item

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```
## Adding Items to a Set

- Add one item using add()

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```
- Add multiple items using update()

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```
## Removing Items from a Set

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```
- The pop() methods remove a random item from a list 

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
```

## Clearing Items in a Set

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```
## Deleting a Set

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```
## Converting List to Set

- Converting set to a list removing duplicates 

```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

## Joining Sets

- Union This method returns a new set

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

- Update This method inserts a set into a given set

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```
## Checking Subset and Super Set

A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```
## Checking the Difference Between Two Sets

# The syntax returns the differences between two sets

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```
## Finding Symmetric Difference Between Two Sets

- It returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```
## Joining Sets

## check if two sets are joint or disjoint using isdisjoint() method.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```
# Day8:
## Dictionaries
## A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

## Creating a Dictionary
```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```
## Dictionary Length
```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```
## Accessing Dictionary Items

- access Dictionary items by referring to its key name
```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
```
- or can access used get method

```py
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
```

## Modifying Items in a Dictionary
```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```
## Checking keys

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```
## Removing Key and Value Pairs
```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
```
## change dictionary to a list of items
```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```
## Clearing a Dictionary

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

## Deleting a Dictionary

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

## Copy a Dictionary

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```
## Getting Dictionary Keys as a List

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```
## Getting Dictionary Values as a List

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```
# Day9:Conditionals

## If condition

Use to check if a condition is true and to execute the block code.

```py
# syntax
if condition:
    this part of code runs for truthy conditions
```

## If Else

If condition is true the first block will be executed, if not the else condition will run. 

```py
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

## If Elif Else

Use elif when have multiple conditions. 

``` py
# syntax
if condition:
    code
elif condition:
    code
else:
    code
```

![Alt text](https://file%2B.vscode-resource.vscode-cdn.net/var/folders/qh/53ry_phd7lv7rdrt9dlzt7_80000gn/T/TemporaryItems/NSIRD_screencaptureui_TrVLIj/Screen%20Shot%202022-11-27%20at%208.19.06%20pm.png?version%3D1669540763820)

Link: https://www.programiz.com/python-programming/if-elif-else

## Shorthand If Else

If only have one statement to execute, one for if, and one for else, can be put on the same line 

``` py
code if condition else code
```

### Nested If

This is when have if statements inside another if statements.

``` py
# syntax
if condition:
    code
    if condition:
    code
``` 
Alternatively, can use logical operator and instead of nested condition. 

## If condition and logical operators

``` py
# syntax
if condition and condition:
    code
``` 
## If and Or 

``` py
# syntax
if condition or condition:
    code
``` 

# Day 10: Loops

To handle repetitive task, programing languages use loops. 

1. while loop
2. for loop

## While loop

- It is used to execute block of statement repeatly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed. 

``` py
 # syntax
while condition:
    code goes here
``` 
- If want to run block of code once the condition is no longer true, use else

``` py
 # syntax
while condition:
    code goes here
else:
    code goes here
``` 

## Break and continute 

- Use break when want to get out or stop the loop

``` py
# syntax
while condition:
    code goes here
    if another_condition:
        break
``` 

- Use continute to skip the current iteration

``` py
 # syntax
while condition:
    code goes here
    if another_condition:
        continue
``` 
## For loop

- loop is used for iterating over a sequence (either a list, a tuple, a dicionary, a set or a string)

``` py
# syntax
for iterator in lst:
    code goes here
``` 

``` py
# syntax
while condition:
    code goes here
    if another_condition:
        break
``` 

``` py
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
``` 
## Range function
- range()function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1.

``` py
# syntax
for iterator in range(start, end, step):
``` 

## Nested for loop 

- write loops inside a loop

``` py
# syntax
for x in y:
    for t in x:
        print(t)
``` 
## For Else

- to execute some message when the loop ends

``` py
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
``` 

## Pass

- use pass to avoid errors or as a placeholder for future statements.

``` py
for number in range(6):
    pass
``` 

# Day 11:

## Functions

### Definition

- Function is a reuseable block of code or programing statements designed to perfom a certain task. Def keyword is use to define a function in Python. 

### Declaring and Calling a Function

``` py
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
``` 

### Function without Parameters

Eg:

``` py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
``` 
### Use return function to return values

``` py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
``` 

### Function with Parameters

- We can pass different data types as a parameter in a function

- Single parameter:

``` py
# syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
  ``` 
Eg: 

``` py
def learner (name):
    message = name + ' is learning Python.'
    return message

print(learner('Tina'))

``` 
- Two Parameter:

``` py
 # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
``` 

Eg:

``` py
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Tina','Bui'))
``` 

### Passing Arguments with Key and Value

``` py
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
``` 

Eg:

``` py
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name(first_name = 'Tina', last_name = 'Bui'))
``` 
### Function with Default Parameters

``` py
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
``` 
Eg:

```py
def learner (name = 'Nancy'):
   message = name + ' is learning Python.'
   return message

print(learner('Tina'))

```
Result: Tina is learning Python.

If we do not pass argument when calling a fucntion, it will return the default value 

```py
def learner (name = 'Nancy'):
   message = name + ' is learning Python.'
   return message

print(learner())

```
Result: Nancy is learning Python.

### Arbitrary Number of Arguments

If do not know the number of arguments pass to a function, can create a function which can take arbitrary number of arguments by adding * before the parameter name.

```py
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

Eg:

```
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

