"""Effect for Al'Akir, the Winds of Time (WON_092h).

Card Text: [x]<b>Battlecry:</b> Draw a <b>Charge</b>,
<b>Divine Shield</b>, <b>Taunt</b>, and
<b>Windfury</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)