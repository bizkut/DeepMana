"""Effect for Savage Ymirjar (RLK_535).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Discard 2 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass