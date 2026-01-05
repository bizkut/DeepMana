"""Effect for Soulbound Ashtongue (BT_727).

Card Text: Whenever this minion takes damage, also deal that amount to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)