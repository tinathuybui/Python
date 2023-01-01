
#Declare an empty list
from audioop import reverse


empty_list = []
print(empty_list)

#Declare a list with more than 5 items
list =["chanel", "gucci", "dior", "ysl","zara","aje"]
print(list)

#Find the length of your list
len(list)

#Get the first item, the middle item and the last item of the list
list =["chanel", "gucci", "dior", "ysl","zara","aje"]
first_item = list[0]
middle_item = list[2]
last_item = list[-1]
print(first_item,middle_item,last_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Tina",27,152,"No","Sydney"]
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
len(it_companies)

#Print the first, middle and last company
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_item = it_companies[0]
middle_item = it_companies[3]
last_item = it_companies[-1]
print(first_item,middle_item,last_item)

#Print the list after modifying one of the companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[0] = 'Optus'
print(it_companies)

#Add an IT company to it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append('Optus')
print(it_companies)


#Insert an IT company in the middle of the companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(3,'Reckon')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
x = it_companies[0]
print(x.upper())

#Join the it_companies with a string '#;  '
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
"; ".join(it_companies)

#Check if a certain company exists in the it_companies list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exist = 'Google' in it_companies
print(does_exist)

#Sort the list using sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(sorted(it_companies))

#Reverse the list in descending order using reverse() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
x = it_companies[0:3]
print(x)

#Slice out the last 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
x = it_companies[4:7]
print(x)

#Slice out the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
x = it_companies[3]
print(x)

#Remove the first IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(3)
print(it_companies)

#Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(7)
print(it_companies)

#Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies
print(it_companies)

#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
x = front_end + back_end
print(x)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = x
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_ages = min(ages)
max_ages = max(ages)
print(ages,min_ages,max_ages)

#Add the min age and the max age again to the list
ages.append('19')
ages.append('26')
print (ages)

#Find the median age (one middle item or two middle items divided by two)
import statistics
print (statistics.median(ages))

#Find the average age (sum of all items divided by their number )
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
from statistics import mean
avg = mean(ages)
print(avg)

#Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
min_ages = min(ages)
max_ages = max(ages)
range = max_ages - min_ages
print(range)

#Compare the value of (min - average) and (max - average), use abs() method
x = min_ages - avg
y = max_ages - avg
print(abs(x))
print(abs(y))
