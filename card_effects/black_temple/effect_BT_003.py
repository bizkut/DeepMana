"""Effect for Netherwind Portal (BT_003).

Card Text: <b>Secret:</b> After your opponent casts a spell, summon a random
4-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_003t")