# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Kitty", "color": "black", "breed": "Poodle", "legs": "4", "age": "3"}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name": "Tina", "last_name": "Bui", "gender": "female", "age": "20", "marital_status": "No", "Skills": ["Python"], "country": "Australia", "city": "Sydney", "address": "Strathfield"}

# Get the length of the student dictionary
len (student)

# Get the value of skills and check the data type, it should be a list --- need to check
print(student['Skills'])
type(student['Skills'])

# Modify the skills values by adding one or two skills
student['Skills'].append("SQL")
student['Skills'].append("Accounting")
print(student)

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student ["first_name"]
# Delete one of the dictionaries
del student