
for i in range(10):
    print('%.2d' %i)

for i in range(10):
    print('%2d' %i)

for i in range(10):
    print('%02d' %i)

for i in range(10):
    print('%2.d' %i)

for i in range(10):
    print('2.%d' %i)

for i in range(10):
    a = 'integer_'
    b = a + str('%02d' %i)
    print(b)
