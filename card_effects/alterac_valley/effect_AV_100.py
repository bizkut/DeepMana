"""Effect for Drek'Thar (AV_100).

Card Text: [x]<b>Battlecry</b>: If this costs
more than every minion in
your deck, summon one
of those minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_100t")