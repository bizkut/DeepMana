"""Effect for Piranha Swarmer (TSC_638).

Card Text: [x]<b>Rush</b>
After you summon a Piranha
Swarmer, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_638t")