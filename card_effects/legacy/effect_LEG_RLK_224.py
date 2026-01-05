"""Effect for Overseer Frigidara (LEG_RLK_224).

Card Text: <b>Battlecry:</b> Draw 2 spells.
If they're both Frost spells, deal 2 damage to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)