"""Effect for Maelstrom Portal (KAR_073).

Card Text: Deal $1 damage to all enemy minions. Summon a random
1-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)