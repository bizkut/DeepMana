"""Effect for Aegwynn, the Guardian (LEG_CS3_001).

Card Text: <b>Spell Damage +2</b>
<b>Deathrattle:</b> The next minion you draw inherits these powers.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(2)