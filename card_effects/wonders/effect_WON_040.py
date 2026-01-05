"""Effect for Disco at the End of Time (WON_040).

Card Text: Cast 5 random <b>Secrets</b> from the past.
At the start of your turn, destroy them.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()