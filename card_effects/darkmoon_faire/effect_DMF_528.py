"""Effect for Tent Trasher (DMF_528).

Card Text: <b><b>Rush</b>.</b> Costs (1) less for each friendly minion with a unique minion type.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass