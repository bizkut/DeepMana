"""Effect for Wolpertinger (SCH_133).

Card Text: <b>Battlecry:</b> Summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_133t")