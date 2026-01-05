"""Effect for Idol of Y'Shaarj (DMF_055).

Card Text: Summon a 10/10 copy of a minion in your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_055t")