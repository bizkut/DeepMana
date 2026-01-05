"""Effect for Harth Stonebrew (GIFT_01).

Card Text: [x]<b>Battlecry:</b> Replace your
hand with an iconic one
from Hearthstone's past.
<i>(Once per game)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass