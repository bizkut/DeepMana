"""Effect for Oondasta (TRL_542).

Card Text: <b>Rush</b>
<b>Overkill:</b> Summon a Beast from your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_542t")