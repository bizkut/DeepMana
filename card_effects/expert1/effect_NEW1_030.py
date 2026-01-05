"""Effect for Deathwing (NEW1_030).

Card Text: <b>Battlecry:</b> Destroy all other minions and discard your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()