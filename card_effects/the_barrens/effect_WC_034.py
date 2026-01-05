"""Effect for Party Up! (WC_034).

Card Text: Summon five 2/2 Adventurers with random bonus effects.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WC_034t")