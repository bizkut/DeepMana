"""Effect for Tasty Flyfish (DRG_049).

Card Text: <b>Deathrattle:</b> Give a Dragon in your hand +2/+2.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2