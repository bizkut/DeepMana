"""Effect for Elven Minstrel (CORE_LOOT_211).

Card Text: <b>Combo:</b> Draw 2 minions from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)