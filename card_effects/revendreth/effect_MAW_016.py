"""Effect for Order in the Court (MAW_016).

Card Text: [x]Reorder your deck from
 highest Cost to lowest
Cost. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)