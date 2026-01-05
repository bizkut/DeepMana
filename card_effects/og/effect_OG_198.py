"""Effect for Forbidden Healing (OG_198).

Card Text: Spend all your Mana. Restore twice that much Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)