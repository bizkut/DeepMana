"""Effect for Flamewreathed Faceless (OG_024).

Card Text: <b>Overload:</b> (2)
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass