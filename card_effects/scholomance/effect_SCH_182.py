"""Effect for Speaker Gidra (SCH_182).

Card Text: [x]<b><b>Rush</b>, Windfury</b>
<b><b>Spellburst</b>:</b> Gain Attack
and Health equal to
the spell's Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)