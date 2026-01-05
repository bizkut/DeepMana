"""Effect for Crackling Razormaw (UNG_915).

Card Text: <b>Battlecry:</b> <b>Adapt</b> a friendly Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass