"""Effect for Bless (AV_329).

Card Text: [x]Give a minion +2 Health,
then set its Attack to be
equal to its Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)