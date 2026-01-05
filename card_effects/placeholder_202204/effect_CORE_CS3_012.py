"""Effect for Nordrassil Druid (CORE_CS3_012).

Card Text: <b>Battlecry:</b> The next spell you cast this turn costs (3) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass