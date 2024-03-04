# Built-in data structures : Dictionaries
# The dictionary is use in data manipulation


# ? Intro to Dictionaries
#Dictionary is defined by the value pairs

my_dict = {'name': 'John', 'age': 24, 'city': 'USA'}

name = my_dict['name']
age = my_dict['age']
print(name)
print(age)

# Add new key values to the dictionaries

my_dict['occupation'] = 'Engineer'
my_dict['experience'] = 2
print(my_dict)

print()
# To remove values using dot notation and del
my_dict.pop('city')
del my_dict['age']
print(my_dict)

print()


# ? Access Python Dictionary Items

my_dict_2 = {'firstname': 'Alice', 'familyName': 'Titi', 'city': 'Canada'}

firstname = my_dict_2['firstname']
familyName = my_dict_2['familyName']

print(firstname)
print(familyName)

# ? using the get method to create a new value IN DICTIONARY

# the get methods returns the value if it is in the dictionary
# unless return null
worker = my_dict_2.get('workers', 'not specified')
print(worker)

# !Using the key and value method, and item method to access and specify
# !each keys and values, and items in the dictionary

keys = my_dict_2.keys()
values = my_dict_2.values()
items = my_dict_2.items()

print(keys)
print(values)
print(items)


# ? How to transform / Change Dictionary Items

my_dict_change = {'firstName': 'Perfect', 'age': '23', 'city': 'London'}

my_dict_change['age'] = 25

my_dict_change.update({'age':29, 'profession': 'Developer'})

new_age = my_dict_change.pop('age')
my_dict_change['age'] = new_age +1

print(my_dict_change)


# ? ADD DICTIONARY ITEMS

add_my_dict = {'firstName': 'Bobo', 'city': 'London',
               'profession': 'Developer', 'age': 30}

# ! adding a new item using bracket notation
add_my_dict['language'] = 'English'

# ! adding new item using the update method
add_my_dict.update({'language': 'German', 'hobby': 'Reading', 'sport': 'Weightlifting'})


# ! using the setdefault method
add_my_dict.setdefault('hobby', 'Reading')


print(add_my_dict)



