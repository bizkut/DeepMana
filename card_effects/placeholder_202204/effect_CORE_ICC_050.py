"""Effect for Webweave (CORE_ICC_050).

Card Text: Summon two 1/2 <b>Poisonous</b> Spiders.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_050t")