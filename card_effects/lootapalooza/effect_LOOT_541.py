"""Effect for King Togwaggle (LOOT_541).

Card Text: [x]<b>Battlecry:</b> Swap decks
with your opponent.
Give them a Ransom
spell to swap back.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1