"""Effect for Threshrider's Blessing (TLC_477).

Card Text: Give a friendly minion +4/+4 and "<b>Deathrattle:</b> Summon a random 4-Cost minion."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_477t")