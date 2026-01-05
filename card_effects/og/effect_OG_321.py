"""Effect for Crazed Worshipper (OG_321).

Card Text: [x]<b>Taunt</b>
Whenever this minion takes
damage, give your C'Thun
+1/+1 <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1