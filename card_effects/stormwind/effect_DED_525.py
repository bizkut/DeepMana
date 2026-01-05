"""Effect for Goliath, Sneed's Masterpiece (DED_525).

Card Text: [x]<b>Battlecry:</b> Fire five rockets
at enemy minions that deal
2 damage each. <i>(You pick
the targets!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)