"""Effect for Doomerang (CORE_ICC_233).

Card Text: Throw your weapon at a minion. It deals its damage, then returns to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)