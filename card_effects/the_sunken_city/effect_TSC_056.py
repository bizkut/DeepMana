"""Effect for Volcanomancy (TSC_056).

Card Text: Choose a minion. When it dies, deal 3 damage to all other minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)