"""Effect for Cavern Shinyfinder (LOOT_033).

Card Text: <b>Battlecry:</b> Draw a weapon from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)