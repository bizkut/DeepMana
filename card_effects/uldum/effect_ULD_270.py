"""Effect for Sandhoof Waterbearer (ULD_270).

Card Text: At the end of your turn, restore #5 Health to a damaged friendly character.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)