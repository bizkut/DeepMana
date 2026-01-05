"""Effect for Cutting Class (SCH_623).

Card Text: [x]Draw 2 cards.
Costs (1) less per Attack
of your weapon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)