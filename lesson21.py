# task 1

words = ['мадам', 'топот', 'test', 'madam', 'word']
# solution 1
new_words = []

for word in words:
    if word == word[::-1]:
        new_words.append(word)

print(new_words)

# solution 2
new_words2 = [word2 for word2 in words if word2 == word2[::-1]]
print(new_words2)


# task 2

my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
new_str = []

for sentence in my_str:
    sentence_r = sentence.replace(' ', '').lower()
    if sentence_r == sentence_r[::-1]:
        new_str.append(sentence)

print(new_str)


# метод str.JOIN

l = list(range(1, 10))
l2 = list('hello')

print(l)

s = '-'.join(map(str, l))   #map() - переводит каждый элемент к определенному типу данных
s2 = ','.join(l2)

print(s)
print(s2)
