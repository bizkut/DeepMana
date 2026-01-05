"""Effect for Soul Split (BT_488).

Card Text: Choose a friendly Demon. Summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_488t")