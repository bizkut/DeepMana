"""Effect for Grave Rune (DRG_302).

Card Text: Give a minion "<b>Deathrattle:</b> Summon 2 copies of this."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_302t")