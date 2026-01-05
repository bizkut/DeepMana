"""Effect for Crooked Cook (CORE_REV_016).

Card Text: [x]At the end of your turn, 
if you dealt 3 or more 
damage to the enemy 
hero, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)