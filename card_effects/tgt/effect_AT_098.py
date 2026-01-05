"""Effect for Sideshow Spelleater (AT_098).

Card Text: <b>Battlecry:</b> Copy your opponent's Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass