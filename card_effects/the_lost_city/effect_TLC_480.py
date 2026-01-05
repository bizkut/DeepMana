"""Effect for Krog, Crater King (TLC_480).

Card Text: [x]At the end of your turn,
set the Attack and Health of
all enemy minions to 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)