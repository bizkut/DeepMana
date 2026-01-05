"""Effect for Glacier Racer (YOP_020).

Card Text: <b>Spellburst</b>: Deal 3 damage to all <b>Frozen</b> enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)