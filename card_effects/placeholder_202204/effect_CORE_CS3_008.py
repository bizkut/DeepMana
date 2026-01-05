"""Effect for Bloodsail Deckhand (CORE_CS3_008).

Card Text: [x]<b>Battlecry:</b> The next
weapon you play costs
(1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass