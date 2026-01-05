"""Effect for E.T.C., God of Metal (DMF_529).

Card Text: After a friendly <b>Rush</b> minion attacks, deal 2 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)