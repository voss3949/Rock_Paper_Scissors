import random
import time

while True:
    choices=[["rock","scissors"],["paper","rock"],["scissors","paper"]]
    computer = random.choice(choices)
    player = ''
    while player not in choices:
        player = input("rock, paper, scissors... GO!")
        break
    time.sleep(3)
    'Loser' if player in computer[1] else 'Winner' if player not in computer else 'Tie'
    time.sleep(3)
    if input('Quit? Yes or No. ') == 'Yes': break
    continue


