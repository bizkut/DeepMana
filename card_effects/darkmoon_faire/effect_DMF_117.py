"""Effect for Cascading Disaster (DMF_117).

Card Text: [x]Destroy a random enemy
minion. <b>Corrupt:</b> Destroy 2.
<b>Corrupt Again:</b> Destroy 3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()