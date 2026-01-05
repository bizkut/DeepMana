"""Effect for Steeldancer (SCH_522).

Card Text: [x]<b>Battlecry:</b> Summon a random
minion with Cost equal to
your weapon's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_522t")