"""Effect for Gormok the Impaler (AT_122).

Card Text: <b>Battlecry:</b> If you have at least 4 other minions, deal 4 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)