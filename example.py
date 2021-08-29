import random

choices=[["rock","scissor"],["paper","rock"],["scissor","paper"]]
computer = random.choice(choices)
self = random.choice(choices)

str('You chose '+self[0])+' '+'Computer chose '+str(computer[0]) if self == computer else "Winner" if self[1] in computer[0] else 'Loser'
