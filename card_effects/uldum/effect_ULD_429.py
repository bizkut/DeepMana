"""Effect for Hunter's Pack (ULD_429).

Card Text: Add a random Hunter Beast, <b>Secret</b>, and weapon to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass