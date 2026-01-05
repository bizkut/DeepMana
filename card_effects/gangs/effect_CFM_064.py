"""Effect for Blubber Baron (CFM_064).

Card Text: Whenever you summon a <b>Battlecry</b> minion while this is in your hand, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_064t")