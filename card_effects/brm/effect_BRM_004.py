"""Effect for Twilight Whelp (BRM_004).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, gain +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)