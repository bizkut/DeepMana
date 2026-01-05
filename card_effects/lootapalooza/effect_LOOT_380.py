"""Effect for Woecleaver (LOOT_380).

Card Text: After your hero attacks, <b>Recruit</b> a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass