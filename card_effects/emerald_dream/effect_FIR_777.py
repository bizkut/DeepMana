"""Effect for Spirit of the Kaldorei (FIR_777).

Card Text: <b>Taunt</b>, <b>Lifesteal</b>
<b>Battlecry:</b> If you used
your Hero Power this
turn, gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3