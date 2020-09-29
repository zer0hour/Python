import random

def game():
    for i in range(1):
        answer = random.randint(1, 20)
        if answer == 1:
            print('It is certain.')
        if answer == 2:
            print('As I see it, yes.')
        if answer == 3:
            print('Reply hazy, try again.')
        if answer == 4:
            print('Don\'t count on it.')
        if answer == 5:
            print('It is decidedly so.')
        if answer == 6:
            print('Most likely.')
        if answer == 7:
            print('Ask again later.')
        if answer == 8:
            print('My reply is no.')
        if answer == 9:
            print('Without a doubt.')
        if answer == 10:
            print('Outlook good.')
        if answer == 11:
            print('Better not tell you now.')
        if answer == 12:
            print('My sources say no.')
        if answer == 13:
            print('Yes - definitely.')
        if answer == 14:
            print('Yes.')
        if answer == 15:
            print('Cannot predict now.')
        if answer == 16:
            print('Outlook not so good.')
        if answer == 17:
            print('You may rely on it.')
        if answer == 18:
            print('Signs point to yes.')
        if answer == 19:
            print('Concentrate and ask again.')
        if answer == 20:
            print('Very doubtful.')

a = 1
while a == 1:
    print('Ask a question.')
    input()
    game()
    print('')
