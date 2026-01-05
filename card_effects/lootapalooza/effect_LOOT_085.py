"""Effect for Rhok'delar (LOOT_085).

Card Text: <b>Battlecry:</b> If your deck has no minions, fill your hand with Hunter spells.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass