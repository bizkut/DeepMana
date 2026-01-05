"""Effect for Ghostly Strike (RLK_573).

Card Text: Deal $1 damage. <b>Combo:</b> Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)