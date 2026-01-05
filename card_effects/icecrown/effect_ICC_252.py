"""Effect for Coldwraith (ICC_252).

Card Text: <b>Battlecry:</b> If an enemy is <b>Frozen</b>, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)