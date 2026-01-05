"""Effect for Bonecaller (RLK_813).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle</b>: Resurrect
a friendly Undead that
died this game.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass