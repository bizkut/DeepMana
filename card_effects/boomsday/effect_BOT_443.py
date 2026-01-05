"""Effect for Void Analyst (BOT_443).

Card Text: <b>Deathrattle:</b> Give all Demons in your hand +1/+1.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1