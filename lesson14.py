# l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
# l2 = list('hello')
# l3 = list((1, 2, 3))
# l4 = [i for i in 'hello']
# l5 = [i for i in 'hello world' if i != ' ']
# l6 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', ' ']]


# print(l1, l2, l3, l4, l5, l6, sep ='\n')

# l6 = list(range(0, 11))
# print(l6)

# for i in range(1, 3):
#     print(f'External cicle #{i}')
#     for j in range(1, 3):
#         print(f'\tInternal cicle #{j}')

print('Таблица умножения:')
for i in range(1,10):
    print(' ')
    for j in range(2,10):
        print(f'{i} * {j} = {i * j}')