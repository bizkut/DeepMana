"""Effect for Kazakus, Golem Shaper (BAR_079).

Card Text: <b>Battlecry:</b> If your deck has no 4-Cost cards, build a custom Golem.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass