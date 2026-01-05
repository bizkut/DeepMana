"""Effect for Chaos Strike (CORE_BT_035).

Card Text: Give your hero +2 Attack this turn. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)