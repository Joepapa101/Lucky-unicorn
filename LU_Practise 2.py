import random
total = 0
cost = 0
print('Welcome to Lucky Unicorn!')
print('This is a random luck game, where you earn money depending which andimal you get')
print('The lucky Unicorn - $5')
print('The Horse is 50 cents')
print('The Zebra is also 50 cents')
print('The Donkey is worth nothing')
enter = input('Press Enter to start')
if enter == '':
   while total <= 10:
    list = ['Unicorn', 'Horse', 'Zebra', 'Donkey']
    unicorn = random.choice(list)
    if unicorn == 'Unicorn':
        print('You got a unicorn:  You win $5')
        total += 5
    elif unicorn == 'Horse':
        print('You got a horse! You win 50 cents!')
        total += 0.5
    elif unicorn == 'Zebra':
        print('You got a Zebra!  You win 50 Cents')
        total += 0.5
    elif unicorn == 'Donkey':
        print('Better luck next time.  You got the Donkey.')
    enter1 = input('Play again? (Y/N)')
    if enter1 == 'Y':
        cost += 0.1
    else:
        print(f'You earned ${total}. ')
        print(f'It cost ${cost}')
        quit()

