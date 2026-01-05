"""Effect for Front Lines (TID_949).

Card Text: [x]Summon a minion
from each player's deck.
Repeat until either side
of the battlefield is full.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TID_949t")