"""Effect for Heart Strike (LEG_RLK_034).

Card Text: Deal $3 damage to
a minion. If that kills it, gain a <b>Corpse</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)