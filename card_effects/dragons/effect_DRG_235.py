"""Effect for Dragonrider Talritha (DRG_235).

Card Text: <b>Deathrattle:</b> Give a Dragon in your hand +3/+3 and this <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3