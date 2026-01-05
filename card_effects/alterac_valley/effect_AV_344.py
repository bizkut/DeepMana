"""Effect for Dun Baldar Bridge (AV_344).

Card Text: [x]After you summon a
minion, give it +2/+2.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_344t")