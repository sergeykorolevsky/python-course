# list.append(x) - добавляет элемент в конец списка
# list.extend(L) - расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x) - вставляет на 1-ый элемент значение х
# list.remove(x) - удаляет первый элемент в списке
# list.pop([i]) - удаляет 1-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]]) - возвращает положение первого элемента со значение х (при этом поиск ведется от start to end)
# list.count(x) - возвращает количество элементов со значением х
# list.sort([key=функция], [reverse=False]) - сортирует список на основе функции
# list.reverse() - разворачивает список
# list.copy() - возвращает копию списка
# list.clear() - очищает список

l = [1, 2, 3, 'hello', ['test', 10], 'world', True]

names = ['Ivanov', 'Petrov', 'Sidorov']

# print(l1[4][0])

l[2] = 'world'
# l[:2] = [10, 15]

# methods:
# l.append('new')
# l.extend([5, 7])
l2 = ['hi', 1]
l += l2
# l.remove('world')
# el = l.pop(2)
# l.sort()

l3 = ['hello', 'hi', 'David', 'world']
# l3.sort()
l3 = sorted(l3)
l.clear()

# print(l, l.count(2), l3, sep='\n')
# print('h' > 'a')
print(l)