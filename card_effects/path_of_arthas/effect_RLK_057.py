"""Effect for Dark Transformation (RLK_057).

Card Text: Transform an Undead into a 4/5 Undead Monstrosity with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass