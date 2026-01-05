"""Effect for Mi'da, Pure Light (ONY_028).

Card Text: [x]<b>Divine Shield</b>, <b>Lifesteal</b>
<b>Deathrattle:</b> Shuffle a Fragment
into your deck that resummons
Mi'da when drawn.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)