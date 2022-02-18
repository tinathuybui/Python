# Python
Learn Python
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
For example to create a sequence of numbers from 3 to 5
1.
x = range(3, 6)
if (n % 2) == 0:# to print even numbers
        if n in range(2,5):
            print("Not Weird")
        if n in range(6,20):
            print("Weird")
        if n > 20:
            print("Not Weird")
    else:
        print("Weird")
        
 2.
  n = int(raw_input())
    for i in range(n):
        print(i**2)# to print square of each numbers


