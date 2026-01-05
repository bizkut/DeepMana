"""Effect for Yogg-Saron, Hope's End (OG_134).

Card Text: [x]<b>Battlecry:</b> Cast a random
spell for each spell you've
cast this game <i>(targets
chosen randomly)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass