"""Effect for Cold Case (REV_505).

Card Text: Summon two 2/2 Volatile Skeletons. Gain 4 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_505t")