"""Effect for Southsea Squidface (OG_267).

Card Text: <b>Deathrattle:</b> Give your weapon +2 Attack.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2