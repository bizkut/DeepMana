"""Effect for Darkfallen Shadow (NX2_051).

Card Text: <b>Rush</b>
<b>Manathirst (6):</b> Gain <b>Reborn</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass