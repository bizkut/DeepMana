"""Effect for Arcane Amplifier (YOD_008).

Card Text: Your Hero Power deals 2 extra damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)