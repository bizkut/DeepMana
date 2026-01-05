"""Effect for To My Side! (LOOT_217).

Card Text: [x]Summon an Animal
Companion, or 2 if your
deck has no minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_217t")