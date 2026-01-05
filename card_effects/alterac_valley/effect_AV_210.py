"""Effect for Pathmaker (AV_210).

Card Text: [x]<b>Battlecry:</b> Cast the other
choice from the last <b>Choose
One</b> spell you've cast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass