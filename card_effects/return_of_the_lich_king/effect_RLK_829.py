"""Effect for Grave Digging (RLK_829).

Card Text: [x]Draw 2 cards.
Costs (1) if a friendly
Undead died after
your last turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)