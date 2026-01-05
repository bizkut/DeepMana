"""Effect for Unearthed Artifacts (TLC_462).

Card Text: [x]Summon a random 2-Cost
minion. If you've <b><b>Discover</b>ed</b>
this turn, summon a random
4-Cost minion instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_462t")