"""Effect for Scourge Illusionist (RLK_217).

Card Text: [x]<b>Deathrattle:</b> Add a 4/4 copy
of another <b>Deathrattle</b> minion
in your deck to your hand.
It costs (4) less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass