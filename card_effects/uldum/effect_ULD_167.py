"""Effect for Diseased Vulture (ULD_167).

Card Text: Whenever your hero takes damage on your turn, summon a random
3-Cost minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_167t")