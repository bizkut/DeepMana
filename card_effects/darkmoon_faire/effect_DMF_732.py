"""Effect for Cenarion Ward (DMF_732).

Card Text: Gain 8 Armor.
Summon a random
8-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_732t")