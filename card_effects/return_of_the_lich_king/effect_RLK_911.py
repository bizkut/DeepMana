"""Effect for From De Other Side (RLK_911).

Card Text: Summon a copy of each minion in your hand.
They attack random enemy minions, then die.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_911t")