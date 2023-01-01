# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
## Find the length of the set it_companies
print(len(it_companies))

## Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

## Insert multiple IT companies at once to the set it_companies
it_companies.update(['Reckon','Alibaba','Huawei'])
print(it_companies)

## Remove one of the companies from the set it_companies
it_companies.remove('Reckon')
print(it_companies)

## What is the difference between remove and discard
### remove syntax will return error if an item does not exist in the set while discard does not return error.  

#Exercises: Level 2
## Join A and B
C = A.union(B)
print(C)

## Find A intersection B
print(A.intersection(B))

## Is A subset of B
print(A.issubset(B))

## Are A and B disjoint sets
print (B.isdisjoint(A))

## Join A with B and B with A
A.update(B)
B.update(A)

## What is the symmetric difference between A and B
print (B.symmetric_difference(A))

## Delete the sets completely
del A
del B
del C

# Exercises: Level 3
## Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print (age_set)
len(age)
len(age_set)

## Explain the difference between the following data types: string, list, tuple and set
-  string
Strings in python are surrounded by either single quotation marks, or double quotation marks
-  list
List items are ordered, changeable, and allow duplicate values.
-  tuple
similar like list but cannot modified once it has been created. Tutples are written with round brackets.
-  set 
is a collection which is unordered, unchangeable*, and unindexed. No duplicate members

## I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split(" ")
print(words)
s = set(words)
print (s)