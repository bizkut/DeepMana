"""Effect for Hullbreaker (DED_505).

Card Text: [x]<b>Battlecry and Deathrattle:</b>
Draw a spell. Your hero takes
damage equal to its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)


def deathrattle(game, source):
    pass