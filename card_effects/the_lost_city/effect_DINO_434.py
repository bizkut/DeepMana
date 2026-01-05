"""Effect for Raptor-Nest Nurse (DINO_434).

Card Text: [x]<b>Battlecry:</b> Get a random
1-Cost minion.
<b><b>Deathrattle:</b> </b>Get a random
1-Cost spell.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass