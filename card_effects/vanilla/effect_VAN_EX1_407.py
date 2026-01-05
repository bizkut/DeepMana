"""Effect for Brawl (VAN_EX1_407).

Card Text: Destroy all minions except one. <i>(chosen randomly)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()