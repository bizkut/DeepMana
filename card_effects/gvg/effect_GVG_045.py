"""Effect for Imp-losion (GVG_045).

Card Text: Deal $2-$4 damage to a minion. Summon a 1/1 Imp for each damage dealt.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)