"""Effect for Princess Huhuran (OG_309).

Card Text: <b>Battlecry:</b> Trigger a friendly minion's <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass