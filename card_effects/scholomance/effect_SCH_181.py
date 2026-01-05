"""Effect for Archwitch Willow (SCH_181).

Card Text: <b>Battlecry:</b> Summon a random Demon from your hand and deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_181t")