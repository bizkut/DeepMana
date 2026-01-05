"""Effect for Flesh Behemoth (RLK_830).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Draw another
Undead and summon
a copy of it.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)