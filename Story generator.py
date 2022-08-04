import random


when = ["Once upon a time", "Yesterday", "Last Sunday", "A long time ago", "A few days ago" ]

who = ['A boy ', 'A man ', 'A cat ', 'A dog ', 'A leapoard ', 'A parrot ']

name = ['Alexander', 'Putin', 'Amaan', 'Guru', 'Alex']

residence = [' India', ' Zaiha', ' SkatePark', ' Singapore', ' Belison', ' Eiffel Tower']

went = [' cinema ', ' college ', ' stadium ', ' chemistry lab ', ' market ']

happened = [' screams out very loud',' did a flip', ' ate Ice-Cream', ' solved a mystery', ' hits someone very badly']

print(random.choice(when) + ' ,' + random.choice(who) + 'coming from' + random.choice(residence) + ', went too the' + random.choice(went) + 'and' + random.choice(happened))