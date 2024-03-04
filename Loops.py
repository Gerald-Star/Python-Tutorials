# what is a loop in Python


# Types of Loops in Python and Use Cases


# While Loop

count = 0
while count < 5:
    print(f'Count: {count}')
    count += 1
    # the while loop will continue executing as long as the count is true

print()

# ? while if

total = 0
while True:
    user_input = input('enter a number (type "exist" to stop):')
    if user_input.lower() == 'exist':
        break
    total += int(user_input)
    print(f'total : {total}')
    
    
# ? while else:
num = 0
while num < 5:
    print(f'num: {num}')
    num += 1
else:
    print('loop completed successfully')    



   

    
