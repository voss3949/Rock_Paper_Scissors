import random

choices=[["rock","scissor"],["paper","rock"],["scissor","paper"]]
choices
computer = random.choice(choices)
computer
self = input('rock, paper, scissors?  ')


'Loser' if self in computer[1] else 'Winner' if self not in computer else 'Tie'


#str('You chose '+self[0])+' '+'Computer chose '+str(computer[0]) if self == computer else "Winner. "+str(self[0])+" beats " + str(computer[1]) if self[1] in computer[0] else 'Loser. ' +str(self[1]+' beats '+computer[0])

#if computer == self:
#    print("You and computer tied. Computer chose "+str(computer[1])+" and you chose "+str(self[1])
#elif self[0] in computer[1]:
#    print("You Win. Computer chose "+str(computer[1]+" and you chose "+str("computer[0])
#else ''
