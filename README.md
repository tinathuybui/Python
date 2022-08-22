
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
- 
```>>> type ((1,2,4,10))
<class 'tuple'>
```
