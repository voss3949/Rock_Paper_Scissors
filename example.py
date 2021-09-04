While True:
    import random
    import time
    choices=[["rock","scissor"],["paper","rock"],["scissor","paper"]]
    choices
    computer = random.choice(choices)
    computer
    self = input('rock, paper, scissors?  ')
    
    'Loser' if self in computer[1] else 'Winner' if self not in computer else 'Tie'
    time.sleep(5)
    continue


