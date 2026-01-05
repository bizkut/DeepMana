"""Effect for Wandering Monster (LOOT_079).

Card Text: <b>Secret:</b> When an enemy attacks your hero, summon a 3-Cost minion as the new target.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_079t")