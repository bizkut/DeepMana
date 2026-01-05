"""Effect for Stranglevine (TLC_465).

Card Text: <b>Deathrattle:</b> Give a random
friendly minion a random
<b>Bonus Effect</b> and this <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1