"""Effect for Hecklebot (DAL_058).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Your opponent summons a minion from their deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_058t")