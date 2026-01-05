"""Effect for Seedcloud Buckler (WC_032).

Card Text: [x]<b>Deathrattle:</b> Give your
 minions <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1