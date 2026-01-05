"""Effect for Dar'Khan Drathir (RLK_539).

Card Text: [x]<b>Lifesteal</b>
At the end of your turn,
deal 6 damage to the
enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)