"""Effect for Vanndar Stormpike (AV_223).

Card Text: [x]<b>Battlecry</b>: If this costs
less than every minion
in your deck, reduce
their Cost by (3).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass