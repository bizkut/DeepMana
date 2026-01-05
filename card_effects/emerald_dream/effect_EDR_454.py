"""Effect for Clutch of Corruption (EDR_454).

Card Text: [x]Choose a friendly Dragon.
Summon a 0/2 Egg that
hatches into a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_454t")