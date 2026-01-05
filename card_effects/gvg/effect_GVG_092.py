"""Effect for Gnomish Experimenter (GVG_092).

Card Text: <b>Battlecry:</b> Draw a card. If it's a minion, transform it into a Chicken.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)