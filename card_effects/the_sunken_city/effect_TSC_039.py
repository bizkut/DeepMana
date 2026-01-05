"""Effect for Azsharan Scavenger (TSC_039).

Card Text: <b>Battlecry:</b> Put a 'Sunken Scavenger' on the bottom of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass