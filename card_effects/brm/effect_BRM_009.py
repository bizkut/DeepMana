"""Effect for Volcanic Lumberer (BRM_009).

Card Text: <b>Taunt</b>
Costs (1) less for each minion that died this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass