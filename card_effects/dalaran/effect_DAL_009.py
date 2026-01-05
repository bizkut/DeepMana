"""Effect for Hagatha's Scheme (DAL_009).

Card Text: Deal $1 damage
to all minions.
<i>(Upgrades each turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)