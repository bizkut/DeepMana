"""Effect for Harbor Scamp (SW_029).

Card Text: <b>Battlecry:</b> Draw a Pirate.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)