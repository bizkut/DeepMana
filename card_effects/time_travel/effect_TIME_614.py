"""Effect for Liferender (TIME_614).

Card Text: <b>Battlecry:</b> If your hero's Health changed this turn, deal 6 damage to an enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)