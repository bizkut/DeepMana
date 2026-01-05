"""Effect for Clockwork Automaton (GIL_646).

Card Text: Double the damage and healing of your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)