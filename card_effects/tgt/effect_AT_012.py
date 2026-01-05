"""Effect for Spawn of Shadows (AT_012).

Card Text: <b>Battlecry and Inspire:</b>
Deal 4 damage to
each hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)