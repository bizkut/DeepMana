"""Effect for Arcane Giant (KAR_711).

Card Text: [x]Costs (1) less for each spell
you've cast this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass