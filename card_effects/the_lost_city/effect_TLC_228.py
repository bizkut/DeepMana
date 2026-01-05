"""Effect for Bralma Searstone (TLC_228).

Card Text: Your Elementals deal
1 extra damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)