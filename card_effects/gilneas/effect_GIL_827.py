"""Effect for Blink Fox (GIL_827).

Card Text: <b>Battlecry:</b> Add a random card to your hand <i>(from your opponent's class).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass