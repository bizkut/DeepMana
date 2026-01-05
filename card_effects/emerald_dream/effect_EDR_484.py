"""Effect for Scavenging Flytrap (EDR_484).

Card Text: After a minion dies,
gain its Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass