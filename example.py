import random
import time

while True:
    choices=[["rock","scissors"],["paper","rock"],["scissors","paper"]]
    choices
    computer = random.choice(choices)
    print("rock, paper, scissors... GO!")
    player = input('rock, paper, scissors?  ')
    time.sleep(3)
    computer[0]
    player
    'Loser' if player in computer[1] else 'Winner' if player not in computer else 'Tie'
    time.sleep(3)
    if input('Quit? Yes or No. ') == 'Yes': break
    continue


