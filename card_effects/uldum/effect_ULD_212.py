"""Effect for Wild Bloodstinger (ULD_212).

Card Text: <b>Battlecry:</b> Summon a minion from your opponent's hand. Attack it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_212t")