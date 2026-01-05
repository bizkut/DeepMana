"""Effect for Vilefiend Trainer (SCH_705).

Card Text: <b>Outcast:</b> Summon two 1/1 Demons.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_705t")