"""Effect for Darkmoon Dirigible (DMF_073).

Card Text: <b>Divine Shield</b>
<b>Corrupt:</b> Gain <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass