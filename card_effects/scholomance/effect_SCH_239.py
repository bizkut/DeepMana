"""Effect for Krolusk Barkstripper (SCH_239).

Card Text: <b>Spellburst:</b> Destroy a random enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()