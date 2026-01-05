"""Effect for Shattered Rumbler (BT_114).

Card Text: <b>Battlecry:</b> If you cast a spell last turn, deal 2 damage to all other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)