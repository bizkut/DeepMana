"""Effect for Val'anyr (LOOT_500).

Card Text: <b>Deathrattle:</b> Give a minion in your hand +4/+2. When it dies, reequip this.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4