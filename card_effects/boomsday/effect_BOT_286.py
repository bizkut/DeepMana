"""Effect for Necrium Blade (BOT_286).

Card Text: <b>Deathrattle:</b> Trigger the <b>Deathrattle</b> of a random friendly minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass