"""Effect for Illusory Greenwing (EDR_260).

Card Text: [x]<b>Taunt</b>. <b>Deathrattle:</b>
Shuffle two 4/5 Dragons with
<b>Taunt</b> into your deck. They're
   <b>Summoned When Drawn</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(4)