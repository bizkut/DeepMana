"""Effect for Direhorn Hatchling (UNG_957).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Shuffle an 8/12 Direhorn with <b>Taunt</b> into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass