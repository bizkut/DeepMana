"""Effect for Fencing Coach (AT_115).

Card Text: <b>Battlecry:</b> The next time you use your Hero Power, it costs (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass