"""Effect for Death Beetle (NX2_010).

Card Text: <b>Taunt</b>
<b>Manathirst (11):</b> Gain +4/+4 and <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 11
        target._max_health += 11