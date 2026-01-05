"""Effect for Lightmaw Netherdrake (ONY_026).

Card Text: <b>Battlecry:</b> If you're holding
a Holy and a Shadow spell, deal 3 damage to all other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)