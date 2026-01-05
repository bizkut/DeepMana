"""Effect for Jerry Rig Carpenter (DED_003).

Card Text: <b>Battlecry:</b> Draw a <b>Choose One</b> spell and split it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)