"""Effect for Chaos Gazer (YOD_027).

Card Text: [x]<b>Battlecry:</b> Curse a
playable card in your
opponent's hand. They
have 1 turn to play it!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass