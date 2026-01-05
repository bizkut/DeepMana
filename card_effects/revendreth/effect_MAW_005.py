"""Effect for Framester (MAW_005).

Card Text: [x]<b>Battlecry:</b> Shuffle 3 'Framed'
cards into the opponent's
deck. When drawn, they
<b>Overload</b> for (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)