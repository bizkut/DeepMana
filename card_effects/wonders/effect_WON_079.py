"""Effect for The Scarab Lord (WON_079).

Card Text: <b>Battlecry:</b> Summon a 0/1 Gong for your opponent.
<b>Combo:</b> Gain <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_079t")