"""Effect for Submerged Spacerock (TID_707).

Card Text: [x]<b>Deathrattle:</b> Add two Arcane
Mage spells to your hand.
They are <b>Temporary</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass