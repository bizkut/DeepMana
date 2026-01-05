"""Effect for Northwatch Commander (BAR_876).

Card Text: <b>Battlecry:</b> If you control a <b>Secret</b>, draw a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)