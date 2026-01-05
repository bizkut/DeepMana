"""Effect for Frenzied Felwing (YOD_032).

Card Text: Costs (1) less for each damage dealt to your opponent this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)