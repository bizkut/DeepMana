"""Effect for Menagerie Warden (KAR_065).

Card Text: <b>Battlecry:</b> Choose a friendly Beast. Summon a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_065t")