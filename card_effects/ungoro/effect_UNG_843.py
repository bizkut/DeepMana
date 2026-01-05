"""Effect for The Voraxx (UNG_843).

Card Text: [x]After you cast a spell on
this minion, summon a
1/1 Plant and cast
another copy on it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_843t")