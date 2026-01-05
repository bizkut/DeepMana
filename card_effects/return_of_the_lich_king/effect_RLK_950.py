"""Effect for Translocation Instructor (RLK_950).

Card Text: [x]<b>Battlecry:</b> Choose an
enemy minion. Swap it
with a random one
in their deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass