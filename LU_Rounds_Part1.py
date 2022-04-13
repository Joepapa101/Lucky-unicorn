import random

TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ''

while play_again != 'x':
    rounds_played += 1
    number = random.randint(6, 36)

    if 1 <= number <= 5:
        token = 'unicorn'
        balance += 4
    elif 6 <= number <= 36:
        token = 'donkey'
        balance -= 1
    else:
        if number % 2 == 0:
            token = 'zebra'
            balance -= 0.5

print()
print(balance)
print(TEST_AMOUNT)
