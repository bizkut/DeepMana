"""Effect for Toreth the Unbreaking (EDR_258).

Card Text: [x]<b>Divine Shield</b>, <b>Taunt</b>
Your <b><b>Divine Shield</b>s</b> take
three hits to break.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass