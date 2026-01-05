"""Effect for Savage Striker (TRL_240).

Card Text: <b>Battlecry:</b> Deal damage to an enemy minion equal to your hero's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)