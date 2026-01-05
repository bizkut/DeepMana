"""Effect for Claw Machine (DMF_069).

Card Text: <b>Rush</b>. <b>Deathrattle:</b> Draw a minion and give it +3/+3.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(3)