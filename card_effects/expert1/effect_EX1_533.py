"""Effect for Misdirection (EX1_533).

Card Text: <b>Secret:</b> When an enemy attacks your hero, instead it attacks another random character.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass