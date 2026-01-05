"""Effect for Muck Hunter (GIL_682).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Summon two 2/1 Mucklings for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_682t")