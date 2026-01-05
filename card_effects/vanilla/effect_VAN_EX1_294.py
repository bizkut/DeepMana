"""Effect for Mirror Entity (VAN_EX1_294).

Card Text: [x]<b>Secret:</b> When
your opponent plays a
minion, summon a copy
of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_EX1_294t")