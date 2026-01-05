"""Effect for Bone Breaker (RLK_516).

Card Text: [x]After your hero attacks a
minion, deal 2 damage
to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)