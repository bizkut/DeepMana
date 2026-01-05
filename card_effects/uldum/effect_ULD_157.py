"""Effect for Questing Explorer (ULD_157).

Card Text: <b>Battlecry:</b> If you control a <b>Quest</b>, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)