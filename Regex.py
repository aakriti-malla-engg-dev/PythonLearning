import re

sentence = "Some API status codes - 200, 404, 500"
y = re.findall('[0-9]+', sentence)
print(y)
y = re.findall('[AEIOU]', sentence)
print(y)


x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
z = re.findall('^F.+:', x)
print(y)
print(z)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
