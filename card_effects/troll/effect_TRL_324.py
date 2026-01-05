"""Effect for Heavy Metal! (TRL_324).

Card Text: [x]Summon a random
minion with Cost equal
to your Armor <i>(up to 10).</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_324t")