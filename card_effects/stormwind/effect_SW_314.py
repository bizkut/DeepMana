"""Effect for Lightbringer's Hammer (SW_314).

Card Text: <b>Lifesteal</b>
Can't attack heroes.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass