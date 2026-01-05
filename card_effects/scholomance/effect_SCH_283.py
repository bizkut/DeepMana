"""Effect for Manafeeder Panthara (SCH_283).

Card Text: <b>Battlecry:</b> If you've used your Hero Power this turn, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)