"""Effect for Awaken the Makers (UNG_940).

Card Text: <b>Quest:</b> Summon
6 <b>Deathrattle</b> minions.<b>
Reward:</b> Amara, Warden of Hope.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_940t")