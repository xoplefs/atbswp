print('Type a name:')
name = input()

age = input('Type your age:')

if name == 'Alice':
    if int(age) > 3000:
        print('You lie!')
    elif int(age) == 56:
        print('Is Alice 56?')
    else:
        print('Garfunkel!')
else:
    print('I don\'t know who the fuck you are!')
