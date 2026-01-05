"""Effect for Dr. Morrigan (BOT_433).

Card Text: <b>Deathrattle:</b> Swap this with a minion from your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass