"""Effect for Plague of Flames (ULD_717).

Card Text: [x]Destroy all your minions.
For each one, destroy a
random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()