"""Effect for Revenge of the Wild (TRL_566).

Card Text: Summon your Beasts that died this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_566t")