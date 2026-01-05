"""Effect for Vivid Spores (BT_101).

Card Text: Give your minions "<b>Deathrattle:</b> Resummon this minion."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_101t")