import random
STARTING_BALANCE = 100
balance = STARTING_BALANCE 
tokens = ['Unicorn',
          'horse', 'horse', 'horse',
          'donkey', 'donkey', 'donkey',
          'zebra', 'zebra', 'zebra']
    
for item in range(100):
    token = random.choice(tokens)


    if token == 'Unicorn':
        balance += 4
    elif token == 'Donkey':
        balance -= 1
    else:
        balance -= .50

print(f'Starting Balance = ${STARTING_BALANCE:.2f}')
print(f'Final Balance = ${balance:.2f}')