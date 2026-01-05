"""Effect for Call of the Wild (OG_211).

Card Text: Summon all three Animal Companions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_211t")