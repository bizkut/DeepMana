"""Effect for Gravelsnout Knight (LOOT_154).

Card Text: <b>Battlecry:</b> Summon a random 1-Cost minion for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_154t")