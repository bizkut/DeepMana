"""Effect for Life Cycle (TLC_235).

Card Text: Destroy a minion. Summon a random minion of the same
Cost to replace it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_235t")