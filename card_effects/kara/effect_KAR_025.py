"""Effect for Kara Kazham! (KAR_025).

Card Text: Summon a 1/1 Candle, 2/2 Broom, and 3/3 Teapot.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_025t")