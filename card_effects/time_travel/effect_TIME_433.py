"""Effect for Cease to Exist (TIME_433).

Card Text: <b>Rewind</b>
<b>Silence</b> and destroy a random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()