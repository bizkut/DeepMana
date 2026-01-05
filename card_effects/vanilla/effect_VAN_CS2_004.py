"""Effect for Power Word: Shield (VAN_CS2_004).

Card Text: Give a minion +2 Health.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)