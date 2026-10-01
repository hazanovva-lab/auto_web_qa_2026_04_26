
new_list = [x if x in 'aeiou' else '*' for x in 'apple']

for item in new_list:
    print(item)