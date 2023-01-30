l1 = [1, 2, 3]
l2 = [i * 2 for i in l1]
print(l2)


l1 = [1, 2, 3]
k = 0
for j in l1:
    k += j ** 2
print(k)


time1 = 3
time2 = 6.7
time3 = 11.8

litres1 = time1 // 2
litres2 = time2 // 2
litres3 = time3 // 2

print(int(litres1), int(litres2), int(litres3))

s = 'Hello world'

if ' ' in s:
    print(s.upper())
else:
    print(s.lower())