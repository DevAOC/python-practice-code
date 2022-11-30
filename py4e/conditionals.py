x = int(input('Number pls: '))
if x < 10:
    print('Yessir')
elif x == 10:
    print('Spot on')
elif x > 10:
    print('Nah bruv')

print('=============')

y = 10
if x <= y:
    print(str(x) + ' is less than or equal to ' + str(y))
elif x >= y:
    print(str(x) + ' is greater than or equal to ' + str(y))

print('=============')

print('Try/except practice')

int1 = None
while isinstance(int1, int) == False:  # isinstance is for type comparison
    print(type(int1))
    try:
        int1 = int(input('Give me a number: '))
    except:
        print('That isn\'t a number!')
print('You\'ve entered ' + str(int1))

print('end of file')
