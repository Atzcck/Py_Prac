import random
def coinflip():
    if random.randint(0,1):
        return 'Heads!'
    else:
        return 'Tails!'
print(coinflip())
