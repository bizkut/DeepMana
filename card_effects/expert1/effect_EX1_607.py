"""Effect for Inner Rage (EX1_607).

Card Text: Deal $1 damage to a minion and give it +2 Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)