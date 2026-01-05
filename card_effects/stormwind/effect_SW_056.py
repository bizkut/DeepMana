"""Effect for Spice Bread Baker (SW_056).

Card Text: <b>Battlecry:</b> Restore Health to your hero equal to your hand size.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)