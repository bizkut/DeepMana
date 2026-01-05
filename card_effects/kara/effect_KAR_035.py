"""Effect for Priest of the Feast (KAR_035).

Card Text: Whenever you cast a spell, restore #3 Health to
your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)