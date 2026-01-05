"""Effect for Ravenous Flock (TLC_232).

Card Text: At the start of your next turn, summon three 2/1 Hatchlings.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_232t")