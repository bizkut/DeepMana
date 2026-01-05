"""Effect for Educated Elekk (SCH_714).

Card Text: [x]Whenever a spell is played,
this minion remembers it.
<b>Deathrattle:</b> Shuffle the
spells into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass