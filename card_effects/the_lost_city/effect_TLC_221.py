"""Effect for Sizzling Swarm (TLC_221).

Card Text: Deal $3 damage.
Summon that many 2/1 Sizzling Cinders.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)