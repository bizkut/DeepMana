"""Effect for Felerin, the Forgotten (RLK_215).

Card Text: [x]<b>Battlecry:</b> Add a random
<b>Outcast</b> card to the left and
right sides of your hand.
They cost (2) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass