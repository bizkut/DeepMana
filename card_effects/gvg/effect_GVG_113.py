"""Effect for Foe Reaper 4000 (GVG_113).

Card Text: Also damages the minions next to whomever it attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass