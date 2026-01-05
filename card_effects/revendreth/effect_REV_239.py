"""Effect for Suffocating Shadows (REV_239).

Card Text: [x]When you play or 
discard this, destroy a 
random enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()