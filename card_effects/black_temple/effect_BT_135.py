"""Effect for Glowfly Swarm (BT_135).

Card Text: Summon a 2/2 Glowfly for each spell in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_135t")