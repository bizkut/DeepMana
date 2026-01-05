"""Effect for Gluttonous Ooze (UNG_946).

Card Text: <b>Battlecry:</b> Destroy your opponent's weapon and gain Armor equal to its Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()