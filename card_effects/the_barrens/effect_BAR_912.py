"""Effect for Apothecary's Caravan (BAR_912).

Card Text: [x]At the start of your turn,
summon a 1-Cost minion
from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_912t")