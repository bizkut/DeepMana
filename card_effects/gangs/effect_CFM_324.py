"""Effect for White Eyes (CFM_324).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Shuffle
'The Storm Guardian' into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass