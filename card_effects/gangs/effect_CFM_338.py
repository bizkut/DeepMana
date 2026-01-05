"""Effect for Trogg Beastrager (CFM_338).

Card Text: <b>Battlecry:</b> Give a random Beast in your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1