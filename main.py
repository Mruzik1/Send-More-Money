from random import sample


# numbering letters
numbers = list(map(lambda x: str(x), sample(range(0, 8), 8)))
numbered_letters = dict(zip(list('SENDMORY'), numbers))

# making a numbered representation of the words
send = int(''.join([numbered_letters[i] for i in 'SEND']))
more = int(''.join([numbered_letters[i] for i in 'MORE']))
money = int(''.join([numbered_letters[i] for i in 'MONEY']))

