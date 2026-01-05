"""Effect for Bolf Ramshield (AT_124).

Card Text: Whenever your hero takes damage, this minion takes it instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass