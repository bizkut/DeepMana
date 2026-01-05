"""Effect for Ship's Chirurgeon (WON_065).

Card Text: After you summon a minion, give it +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_065t")