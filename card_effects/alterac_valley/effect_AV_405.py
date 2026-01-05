"""Effect for Contraband Stash (AV_405).

Card Text: Replay 5 cards from other classes you've played this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass