"""Effect for Felfire Blaze (FIR_904).

Card Text: [x]After you cast a Fel spell,
destroy this and deal 2
damage to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)