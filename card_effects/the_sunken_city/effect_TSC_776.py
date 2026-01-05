"""Effect for Azsharan Sweeper (TSC_776).

Card Text: <b>Battlecry:</b> Put a 'Sunken Sweeper' on the bottom of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass