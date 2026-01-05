"""Effect for Deck of Wonders (LOOT_106).

Card Text: Shuffle 5 Scrolls into your deck. When drawn, cast a random spell.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)