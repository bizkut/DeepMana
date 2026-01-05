"""Effect for Creep Tumor (SC_011).

Card Text: Your Zerg minions have +1 Attack and <b>Rush</b>. Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
