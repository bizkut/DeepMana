"""Effect for Ragnaros, Lightlord (CORE_OG_229).

Card Text: At the end of your turn, restore #8 Health to a damaged friendly character.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)