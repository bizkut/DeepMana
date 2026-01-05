"""Effect for Deliverance (AV_315).

Card Text: Deal $3 damage to a minion. <b>Honorable Kill:</b> Summon a new 3/3
copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)