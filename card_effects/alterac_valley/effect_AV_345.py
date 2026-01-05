"""Effect for Saidan the Scarlet (AV_345).

Card Text: <b>Rush.</b> Whenever this minion gains Attack or Health, double that amount <i>(wherever this is)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)