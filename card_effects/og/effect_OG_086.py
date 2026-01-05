"""Effect for Forbidden Flame (OG_086).

Card Text: Spend all your Mana. Deal that much damage to a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)