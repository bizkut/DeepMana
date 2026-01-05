"""Effect for Wildfire (BAR_546).

Card Text: [x]Your Hero Power
deals 1 more damage
this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)