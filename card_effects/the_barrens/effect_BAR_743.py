"""Effect for Toad of the Wilds (BAR_743).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you're holding
a Nature spell, gain
+2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)