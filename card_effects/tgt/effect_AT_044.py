"""Effect for Mulch (AT_044).

Card Text: Destroy a minion.
Add a random minion to your opponent's hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()