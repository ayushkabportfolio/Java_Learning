x = 'Hi there hello'
words = x.split(' ')
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])
print(' '.join(reversed_words))