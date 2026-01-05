"""Effect for Solid Alibi (REV_504).

Card Text: Until your next turn, your hero can only take 1 damage at a time.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass