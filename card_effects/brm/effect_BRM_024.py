"""Effect for Drakonid Crusher (BRM_024).

Card Text: <b>Battlecry:</b> If your opponent has 15 or less Health, gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 15, source)