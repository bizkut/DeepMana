"""Effect for Ransack (NX2_004).

Card Text: Deal $1 damage to a minion. If you've played a card from another class this turn, deal $4 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)