"""Effect for Shiver Their Timbers! (SW_027).

Card Text: Deal $2 damage to a minion. If you control a Pirate, deal $5 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)