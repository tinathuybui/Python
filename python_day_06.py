#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Vi','Tien','Thuy')
brothers = ('Dat', 'Dinh', 'Tien')

#Join brothers and sisters tuples and assign it to siblings
brothers_sisters = sisters + brothers

#How many siblings do you have?
len(brothers_sisters)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(brothers_sisters)
family_members.append('Thuy')
family_members = tuple(family_members)

#Unpack siblings and parents from family_members
sisters = family_members [0:3]
brothers = family_members [3:5]
mom = family_members[6]

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'grape', 'watermelon','orange')
vegetables = ('kale', 'spinach')
animals = ('chicken', 'cow', 'pig')
food_stuff_tp = fruits + vegetables + animals

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len(food_stuff_lt)
middle_items = food_stuff_lt[4]

#Slice out the first three items and the last three items from food_staff_lt list
fist_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[6:9]

#Delete the food_staff_tp tuple completely
del food_staff_tp

#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries )
print('Iceland' in nordic_countries )