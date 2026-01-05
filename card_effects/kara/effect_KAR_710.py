"""Effect for Arcanosmith (KAR_710).

Card Text: <b>Battlecry:</b> Summon a 0/5 minion with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_710t")