#     Loops and Iterations

#     while loop
# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
#
# print('exit')
# print(n)

#     breaking out of a loop
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

#     finishing an iteration with continue
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

#     for loop
# for i in [1, 2, 3, 4, 5]:
#     print(i)
# print('best!')
#
# friends = ['a', 'b', 'c']
# for friend in friends:
#     print('Happy New Year, ', friend)

#     finding the largest number through iteration
# largest_so_far = -1
# for the_num in [1,14,15,3,56,99,87]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
#     print('Largest: ', largest_so_far)


#    finding the smallest value
# smallest_so_far = None
# for value in [9,4,6,3,2,8]:
#     if smallest_so_far is None:
#         smallest_so_far = value
#     elif value < smallest_so_far:
#         smallest_so_far = value
#     print(smallest_so_far, value)


# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the
# total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

# count = 0
# total = 0.0
# while True:
#     number = input('Enter a number: ')
#     if number == 'done':
#         break
#     try:
#         float_val = float(number)
#     except:
#         print('Invalid input')
#         continue
#     count = count + 1
#     total = float_val + total
# print(total, count, total / count)

#     prints maximum and minimum
# smallest = None
# largest = None
# total = 0.0
# while True:
#     number = input('Enter a number: ')
#     if number == 'done':
#         break
#
#     try:
#         float_val = float(number)
#         number = int(number)
#         total = float_val + total
#         if smallest is None or number < smallest:
#             smallest = number
#         elif largest is None or number > largest:
#             largest = number
#     except:
#         print('Invalid input')
#         continue
#
#
# print(total, largest, smallest)

# Looping and counting

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)


# strings

# parsing and Extracting
# data = 'from aakriti.malla@moengage.com Thru Feb'
# atpos = data.find('@')
# sppos = data.find(' ', atpos)
# host = data[atpos+1:sppos]
# print(host)

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     mintues = (seconds - hours * 3600) // 60
#     remaining = seconds - hours * 3600 - mintues * 60
#     return hours, mintues, remaining
#
#
# print(convert_seconds(5000))

# A function is created with the def() keyword. The parameter
# variable "time_as_string" is passed to the function through a
# call to the function.
# def task_reminder(time_as_string):
#     if time_as_string == "8:00 a.m.":
#         task = "Check overnight backup images"
#     elif time_as_string == "11:30 a.m.":
#         task = "Run TPS report"
#     elif time_as_string == "5:30 p.m.":
#         task = "Reboot servers"
#     else:
#         task = "Provide IT Support to employees"
#     return task
#
#
# print(task_reminder("10:00 a.m."))

#
# num1 = 0
# num2 = 0
#
# for x in range(5):
#     num1 = x
#     for y in range(14):
#         num2 = y + 3
#
# print(num1 + num2)

# changing domain name
# def replace_domain(email, old_domain, new_domain):
#     if '@' + old_domain in email:
#         index = email.index('@' + old_domain)
#         new_email = email[:index] + '@' + new_domain
#         return new_email
#     return email
#
#
# print(replace_domain('aakritimalla@gmail.com', 'gmail.com', 'moengage.com'))

# formatting methods
#
# price = 100
# with_tax = price * 1.05
# print("price: ${:.2f} and with tax total price: ${:.2f}".format(price, with_tax))


# F to cel

# def to_celsius(x):
#     return (x - 32) * 5 / 9
#
#
# for x in range(0, 100, 10):
#     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# dictionaries

# file_counts = {'jpg': 10, 'png': 11, 'txt': 4, 'csv': 6}
# for ext in file_counts:
#     print(ext)

# for ext, amount in file_counts.items():
#     print('There are {} files for .{} extension'.format(amount, ext))

# print(file_counts.keys())
# print(file_counts.values())

# How many times a letter appears in a piece of text?

# def count_letters(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result
#
#
# print(count_letters('Hello Aakriti'.upper()))

# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.

# def sum_server_time(Server):
#     total_time = 0.0
#     for key, val in Server.items():
#         total_time += Server[key]
#
#     return round(total_time, 2)
#
#
# FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
#
# print(sum_server_time(FileServer))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
#
# print(wardrobe)


# car_make = "Lamborghini"
# print(car_make[3:-5])
# print(car_make[-4:])
# print(car_make[:7])



