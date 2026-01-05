"""Effect for Vitality Totem (GVG_039).

Card Text: At the end of your turn, restore #4 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)