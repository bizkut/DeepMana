"""Effect for Corpsetaker (CORE_ICC_912).

Card Text: [x]<b>Battlecry:</b> Gain <b>Taunt</b> if your
deck has a <b>Taunt</b> minion.
Repeat for <b>Divine Shield</b>,
<b>Lifesteal</b>, <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass