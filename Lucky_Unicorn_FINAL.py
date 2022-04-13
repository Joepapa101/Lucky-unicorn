#Lucky Unicorn Projet Version 1.0 Beta
#Copyright 2022 Joshua Currie-Cook

#Starting Libraries
import time
import random

#Program and version
print('******************************************************')
print('***********LUCKY UNICORN VERSION 1.0 STABLE***********')
print('*********Copyright 2022 Joshua Currie-Cook************')
print('******************************************************')


#rules
print('')
print('')
print('')
print('Welcome to Lucky Unicorn!')
print('Here are the rules:')
print('')
time.sleep(1)
print('Unicorns are worth $4')
print('Donkeys and zebras take 50 cents off your total')
print('Horses are worth nothing')
print('It costs $1 for each round, and you can put in as much money as you want')
print('Your aim is to get as many Unicorns as possible and try to avoid the Donkeys and horses')
print('You can withdraw your money at any time')
print('Anyway, without further or do, lets get on to it')
print('')
print('')
time.sleep(3)


#Variables
STARTING_BALANCE = int(input('Enter amount of money:  $'))
balance = STARTING_BALANCE
count = STARTING_BALANCE

user = input('Press enter to start ')


#main routine
while count != 0:
    number = random.randint(1, 100)
    #If the [random] number is below 5, then give the user the unicorn token, giving them $4 bonus
    if 1 <= number <= 5:
        token = 'unicorn'
        balance += 4
        count -= 1
    #If the random number is between 6 and 36, then give the user a donkey token, taking 50 cents off their total
    elif 6 <= number <= 36:
        token = 'donkey'
        balance -= 1
        count -= 1
    #If the random number is between 37 and 100, then give the user a zebra if the random number is divisible by 2.  Otherwise give them a horse.
    else:
        if number % 2 == 0:
            token = 'zebra'
            balance -= 0.5
            count -= 1
        else: 
            token = 'horse'
            balance -= .5
            count -= 1
    #Print commands to print the variables to keep the user updated on their totals as they play
    print(f'You got {token}')
    print(f'Your current balance is ${balance}')
    user1 = input('Continue?  Y/N:  ')
    if user1 == 'N':
        print('You ended early')
#ending routine        
        print('Thanks for playing')
        print(f'You have {balance} dollars')
        quit()
if balance >= STARTING_BALANCE:
    print(f'You get ${balance} dollars! Good job!')
    quit()
else:
    print(f'Better luck next time.  You have {balance} dollars')
    quit()
