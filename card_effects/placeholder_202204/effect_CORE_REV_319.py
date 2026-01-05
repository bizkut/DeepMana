"""Effect for Sesselie of the Fae Court (CORE_REV_319).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle</b>: Draw a minion.
Reduce its Cost by (8).
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(8)