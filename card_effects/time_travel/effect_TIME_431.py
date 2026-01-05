"""Effect for Amber Priestess (TIME_431).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Restore Health
to a character equal to
this minion's Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)