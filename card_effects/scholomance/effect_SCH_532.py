"""Effect for Goody Two-Shields (SCH_532).

Card Text: <b>Divine Shield</b>
<b>Spellburst:</b> Gain <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass