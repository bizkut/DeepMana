"""Effect for Blood in the Water (TSC_932).

Card Text: Deal $3 damage to an enemy. Summon a 5/5 Shark with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)