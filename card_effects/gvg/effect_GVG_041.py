"""Effect for Dark Wispers (GVG_041).

Card Text: <b>Choose One -</b> Summon 5 Wisps; or Give a minion +5/+5 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_041t")