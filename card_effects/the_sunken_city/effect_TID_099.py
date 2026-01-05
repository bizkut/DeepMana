"""Effect for K9-0tron (TID_099).

Card Text: [x]<b>Battlecry:</b> <b>Dredge</b>.
If it's a 1-Cost minion,
summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TID_099t")