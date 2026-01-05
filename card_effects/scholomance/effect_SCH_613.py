"""Effect for Groundskeeper (SCH_613).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you're holding a
spell that costs (5) or more,
restore 5 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)