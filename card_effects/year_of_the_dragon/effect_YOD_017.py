"""Effect for Shadow Sculptor (YOD_017).

Card Text: <b>Combo:</b> Draw a card for each card you've played this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)