"""Effect for EVIL Genius (DAL_606).

Card Text: <b>Battlecry:</b> Destroy a friendly minion to add 2 random <b>Lackeys</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()