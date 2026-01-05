"""Effect for Breath of Dreams (DRG_318).

Card Text: Draw a card. If you're holding a Dragon, gain an empty Mana Crystal.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)