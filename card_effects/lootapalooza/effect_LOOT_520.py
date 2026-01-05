"""Effect for Seeping Oozeling (LOOT_520).

Card Text: <b>Battlecry:</b> Gain the <b>Deathrattle</b> of a random minion in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass