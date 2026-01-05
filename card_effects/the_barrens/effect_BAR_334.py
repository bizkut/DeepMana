"""Effect for Overlord Saurfang (BAR_334).

Card Text: <b>Battlecry:</b> Resurrect 2 friendly <b>Frenzy</b> minions. Deal 1 damage to all other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)