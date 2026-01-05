"""Effect for Snapjaw Shellfighter (TRL_535).

Card Text: [x]Whenever an adjacent
minion takes damage, this
 minion takes it instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass