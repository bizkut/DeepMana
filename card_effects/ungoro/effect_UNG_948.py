"""Effect for Molten Reflection (UNG_948).

Card Text: Choose a friendly minion. Summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_948t")