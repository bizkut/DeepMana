"""Effect for Sanguine Depths (REV_990).

Card Text: [x]Deal 1 damage to a 
minion and give it 
+2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)