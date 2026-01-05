"""Effect for Spark Drill (BOT_102).

Card Text: <b>Rush</b>
<b>Deathrattle:</b> Add two
1/1 Sparks with <b>Rush</b> to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass