"""Effect for Shaky Zipgunner (CFM_336).

Card Text: [x]<b>Deathrattle:</b> Give a random
minion in your hand +2/+2.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2