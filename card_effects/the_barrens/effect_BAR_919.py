"""Effect for Neeru Fireblade (BAR_919).

Card Text: <b>Battlecry:</b> If your deck is empty, open a portal that fills your board with 3/2 Imps each turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass