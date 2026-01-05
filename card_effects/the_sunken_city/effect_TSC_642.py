"""Effect for Trench Surveyor (TSC_642).

Card Text: <b>Battlecry:</b> <b>Dredge</b>.
If it's a Mech, draw it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)