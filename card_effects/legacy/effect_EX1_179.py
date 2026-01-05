"""Effect for Icicle (EX1_179).

Card Text: Deal $2 damage to a minion. If it's <b>Frozen</b>, draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)