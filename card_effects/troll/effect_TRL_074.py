"""Effect for Serrated Tooth (TRL_074).

Card Text: <b>Deathrattle:</b> Give your minions <b>Rush</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1