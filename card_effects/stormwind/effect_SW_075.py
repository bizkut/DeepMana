"""Effect for Elwynn Boar (SW_075).

Card Text: [x]<b>Deathrattle:</b> If you had 7
Elwynn Boars die this game,
equip a 15/3 Sword of a
   Thousand Truths.@ <i>(@/7)</i>
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass