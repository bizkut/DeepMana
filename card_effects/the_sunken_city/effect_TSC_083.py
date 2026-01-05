"""Effect for Seafloor Savior (TSC_083).

Card Text: [x]<b>Battlecry:</b> <b>Dredge</b>.
If it's a minion, give it
this minion's Attack
and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)