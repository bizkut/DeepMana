"""Effect for Beastmaster Leoroxx (BT_214).

Card Text: <b>Battlecry:</b> Summon 3 Beasts from your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_214t")