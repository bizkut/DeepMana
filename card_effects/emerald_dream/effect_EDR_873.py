"""Effect for Envoy of the Glade (EDR_873).

Card Text: [x]<b>Battlecry:</b> Transform all
Neutral cards in your deck
 into random Druid ones.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass