tries = 0
while True:
    if input('> ') == 'exit':
        break
    tries += 1
    print('Attempted to break out ' + str(tries) + ' times.')


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in arr:
    if i % 2 == 0:
        print(i)
