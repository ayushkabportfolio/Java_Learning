x = ['Apple','Banana','Orange','Kiwi','Apple','Grapes','Kiwi','Orange','Apple']

word = 'Apple'
occurance = 2
count = 0

for i in range(0,len(x)):
    if x[i] == word:
        count = count+1
        if count == occurance:
            del x[i]
            break

print(x)