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

