import random
import time

while True:
    choices=[["rock","scissors"],["paper","rock"],["scissors","paper"]]
    computer = random.choice(choices)
    player = ''
    while player not in choices:
        player = input("rock, paper, scissors... GO!  ")
        break
    time.sleep(3)
    'Loser! Computer chose ' + computer[0] if player in computer[1] else 'Winner! Computer chose ' + computer[0] if player not in computer else 'Tie! Compupter chose ' + computer[0]
    time.sleep(3)
    if input('Quit? Yes or No. ') == 'Yes': break
    continue


