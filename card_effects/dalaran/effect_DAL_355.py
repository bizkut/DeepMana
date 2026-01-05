"""Effect for Lifeweaver (DAL_355).

Card Text: Whenever you restore Health, add a random Druid spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)