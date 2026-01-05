"""Effect for Illuminator (GVG_089).

Card Text: If you control a <b>Secret</b> at the end of your turn, restore #4 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)