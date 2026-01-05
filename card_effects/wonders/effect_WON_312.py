"""Effect for Wickerflame Burnbristle (WON_312).

Card Text: <b>Taunt</b>
<b>Divine Shield</b>
<b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass