"""Effect for Rotting Necromancer (NX2_018).

Card Text: <b>Battlecry:</b> <b>Dredge.</b> If it's an Undead, deal 5 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)