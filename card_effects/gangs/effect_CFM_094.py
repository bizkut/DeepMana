"""Effect for Felfire Potion (CFM_094).

Card Text: Deal $5 damage to all characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)