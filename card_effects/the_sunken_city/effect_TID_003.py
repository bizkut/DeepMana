"""Effect for Tidelost Burrower (TID_003).

Card Text: <b>Battlecry:</b> <b>Dredge</b>.
If it's a Murloc, summon a 2/2 copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TID_003t")