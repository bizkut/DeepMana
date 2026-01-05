"""Effect for Test Subject (BOT_558).

Card Text: [x]<b>Deathrattle:</b> Shuffle any
spells you cast on this
minion into your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass