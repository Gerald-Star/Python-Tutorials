# for loops
# ? Use Cases
'''
Using for loops helps to print an argument several time
# and reduce repetitions
'''
print('Hello')
print('Hello')
print('Hello')
print('Hello')
'''
# x is the temp value use to store the current value 

# x is the temp value use to store the current value 

'''
# x is the temp value use to store the current value
for x in range(0, 5):
    print('Hello')

for name in range(0, 4):
    print(f'Hello {name}')

print()

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(f'I like {fruits}')

print()

for number in range(1, 6):
    print(f'count: {number}')

    for index, fruit in enumerate(fruits):
        print(f'Index: {index}, Fruit: {fruit}')
student = 'Danny'
for name_student in student:
    print(student)
print()

# for loop in a Python list
students = ['Manny', 'Ola', 'Gloria']
for names in students:
    print(names)
    print(f'Who is {names}?')

print()

# for loop in a Python Tuple
student_names = ('Angela', 'Ola', 'Gloria')
for mention in student_names:
    print(f'Hello {mention}!')

print()

for i in range(1, 13):
    for z in range(1, 13):
        print(f'{i} X {z} = {i * z}')
        print('=======')
