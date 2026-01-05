"""Effect for Stand Against Darkness (OG_273).

Card Text: Summon five 1/1 Silver Hand Recruits.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_273t")