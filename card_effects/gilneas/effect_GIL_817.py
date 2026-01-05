"""Effect for The Glass Knight (GIL_817).

Card Text: [x]<b>Divine Shield</b>
Whenever you restore Health,
gain <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)