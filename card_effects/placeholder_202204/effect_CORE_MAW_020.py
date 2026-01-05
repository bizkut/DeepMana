"""Effect for Scribbling Stenographer (CORE_MAW_020).

Card Text: <b>Rush</b>. Costs (1) less for each card you've played this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass