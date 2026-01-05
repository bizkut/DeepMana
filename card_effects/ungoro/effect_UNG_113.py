"""Effect for Bright-Eyed Scout (UNG_113).

Card Text: <b>Battlecry:</b> Draw a card. Change its Cost to (5).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)