while True:
    import random
    import time
    choices=[["rock","scissors"],["paper","rock"],["scissors","paper"]]
    choices
    computer = random.choice(choices)
    self = input('rock, paper, scissors?  ')
    self
    computer
    'Loser' if self in computer[1] else 'Winner' if self not in computer else 'Tie'
    time.sleep(5)
    if input('Quit? Yes or No.') == 'Yes': break
    continue


