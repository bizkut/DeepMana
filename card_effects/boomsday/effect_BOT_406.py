"""Effect for Supercollider (BOT_406).

Card Text: [x]After you attack a minion,
force it to attack one
of its neighbors.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass