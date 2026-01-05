"""Effect for Quick Shot (BRM_013).

Card Text: Deal $3 damage.
If your hand is empty, draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)