"""Effect for Touch of the Nathrezim (SW_090).

Card Text: [x]Deal $2 damage to a
minion. If it dies, restore
3 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)