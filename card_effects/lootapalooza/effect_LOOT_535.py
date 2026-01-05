"""Effect for Dragoncaller Alanna (LOOT_535).

Card Text: <b>Battlecry:</b> Summon a 5/5 Dragon for each spell you cast this game that costs (5) or more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_535t")