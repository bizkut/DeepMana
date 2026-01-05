"""Effect for Bloodsworn Mercenary (ULD_720).

Card Text: [x]<b>Battlecry</b>: Choose a
damaged friendly minion.
Summon a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_720t")