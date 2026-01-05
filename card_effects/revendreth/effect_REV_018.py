"""Effect for Prince Renathal (REV_018).

Card Text: Your deck size and
starting Health are 40.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 40, source)