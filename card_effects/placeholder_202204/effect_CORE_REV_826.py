"""Effect for Private Eye (CORE_REV_826).

Card Text: [x]<b>Battlecry:</b> Cast a <b>Secret</b>
from your deck.
 <b>Combo:</b> Cast 2 instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass