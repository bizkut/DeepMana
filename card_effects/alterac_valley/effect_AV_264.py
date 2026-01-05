"""Effect for Sigil of Reckoning (AV_264).

Card Text: At the start of your next turn, summon a random Demon from your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_264t")