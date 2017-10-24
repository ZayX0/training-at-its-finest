def userInput():
    while True:
        userNum = input('Put in a number and I can tell you if it\'s odd or even: ')
        try:
            convertNum = int(userNum)
            break
        except:
            print('That\'s not something I was expecting, try again')
    return convertNum

goodNumber = userInput()

if goodNumber % 2 == 0:
    print('Your number is even!')
else:
    print('Your number is odd!')
