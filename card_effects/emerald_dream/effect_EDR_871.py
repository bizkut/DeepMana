"""Effect for Spirit Gatherer (EDR_871).

Card Text: <b>Battlecry:</b> Get a Wisp. <b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass