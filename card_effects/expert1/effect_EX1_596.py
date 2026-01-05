"""Effect for Demonfire (EX1_596).

Card Text: Deal $2 damage to a minion. If it’s a friendly Demon, give it +2/+2 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)