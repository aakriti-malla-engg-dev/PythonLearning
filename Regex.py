import re

sentence = "From Am to Pm"
check = re.search('^From', sentence)
if check:
    print('yes!')
else:
    print('No')
