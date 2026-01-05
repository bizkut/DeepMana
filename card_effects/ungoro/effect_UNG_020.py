"""Effect for Arcanologist (UNG_020).

Card Text: <b>Battlecry:</b> Draw a <b>Secret</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)