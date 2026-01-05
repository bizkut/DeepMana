"""Effect for Oracle of Elune (SW_419).

Card Text: [x]After you play a minion
that costs (2) or less,
summon a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_419t")