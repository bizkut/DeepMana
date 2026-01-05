"""Effect for Witching Hour (GIL_571).

Card Text: Summon a random friendly Beast that died this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_571t")