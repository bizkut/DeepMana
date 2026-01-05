"""Effect for Escape Pod (GDB_877).

Card Text: [x]<b>Rush</b>  <b>Deathrattle:</b> Give adjacent  minions +1/+1 and <b>Rush</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent
    pass
