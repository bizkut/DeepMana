"""Effect for Holy Wrath (VAN_EX1_365).

Card Text: Draw a card and deal damage equal to its Cost.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)