"""Effect for Vicious Fledgling (UNG_075).

Card Text: After this minion attacks a hero, <b>Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass