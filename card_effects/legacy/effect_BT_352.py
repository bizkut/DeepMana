"""Effect for Satyr Overseer (BT_352).

Card Text: After your hero attacks, summon a 2/2 Satyr.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_352t")