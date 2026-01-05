"""Effect for First Blade of Wrynn (SW_305).

Card Text: [x]<b>Divine Shield</b>
<b>Battlecry:</b> Gain <b>Rush</b> if this
has at least 4 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass