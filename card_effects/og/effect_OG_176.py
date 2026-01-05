"""Effect for Shadow Strike (OG_176).

Card Text: Deal $5 damage to an undamaged character.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)