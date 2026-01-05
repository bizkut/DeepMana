"""Effect for Wispering Woods (GIL_553).

Card Text: [x]Summon a 1/1 Wisp for
each card in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_553t")