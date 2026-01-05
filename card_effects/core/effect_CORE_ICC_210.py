"""Effect for Shadow Ascendant (CORE_ICC_210).

Card Text: [x]At the end of your turn, give another random friendly minion +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
