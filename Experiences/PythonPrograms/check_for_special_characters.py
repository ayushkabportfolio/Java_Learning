x = 'Hi there^^* men'
special_characters = "!@#$%^&*()-+?_=,<>/"
special_found = False


for char in x:
    if char in special_characters:
        special_found = True
        break
if special_found == True:
    print("Yes")
else:
    print('No')