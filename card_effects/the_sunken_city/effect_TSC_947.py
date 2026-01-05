"""Effect for Naga's Pride (TSC_947).

Card Text: Summon two 2/2 Lionfish. If you played a Naga while holding this, give them +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_947t")