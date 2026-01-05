"""Effect for Cookie the Cook (DED_522).

Card Text: [x]<b>Lifesteal</b>
<b>Deathrattle:</b> Equip a 2/3
  Stirring Rod with <b>Lifesteal</b>. 
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass