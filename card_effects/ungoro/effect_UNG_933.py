"""Effect for King Mosh (UNG_933).

Card Text: <b>Battlecry:</b> Destroy all damaged minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()