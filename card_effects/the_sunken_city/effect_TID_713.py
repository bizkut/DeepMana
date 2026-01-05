"""Effect for Bubbler (TID_713).

Card Text: [x]After this minion takes
 exactly one damage,
destroy it. <i>(Pop!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()