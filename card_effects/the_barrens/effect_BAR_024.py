"""Effect for Oasis Thrasher (BAR_024).

Card Text: <b>Frenzy:</b> Deal 3 damage to the enemy hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)