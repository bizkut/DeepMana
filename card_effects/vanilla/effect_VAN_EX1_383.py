"""Effect for Tirion Fordring (VAN_EX1_383).

Card Text: <b><b>Divine Shield</b>,</b> <b>Taunt</b> <b>Deathrattle:</b> Equip a 5/3 Ashbringer.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass