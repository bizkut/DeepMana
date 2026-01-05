"""Effect for Ironforge Portal (KAR_091).

Card Text: Gain 4 Armor.
Summon a random
4-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_091t")