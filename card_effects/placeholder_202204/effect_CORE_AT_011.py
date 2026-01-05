"""Effect for Holy Champion (CORE_AT_011).

Card Text: <b>Overheal:</b> Gain +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)