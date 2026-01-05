"""Effect for Vivid Nightmare (GIL_813).

Card Text: [x]Choose a friendly minion.
Summon a copy of it with
1 Health remaining.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_813t")