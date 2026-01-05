"""Effect for ZOMBEEEES!!! (NX2_013).

Card Text: <b>Secret:</b> After your opponent plays a minion, summon four 1/1 Zombees to attack it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_013t")