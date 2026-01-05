"""Effect for Countess Ashmore (GIL_578).

Card Text: [x]<b>Battlecry:</b> Draw a <b>Rush</b>,
<b>Lifesteal</b>, and <b>Deathrattle</b>
card from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)


def deathrattle(game, source):
    pass