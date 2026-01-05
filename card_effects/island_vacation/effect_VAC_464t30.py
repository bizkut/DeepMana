"""Effect for Hilt of Quel'Delar (VAC_464t30).

Card Text: Give a minion +3/+3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
