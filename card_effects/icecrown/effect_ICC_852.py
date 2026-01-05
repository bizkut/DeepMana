"""Effect for Prince Taldaram (ICC_852).

Card Text: <b>Battlecry:</b> If your deck has no 3-Cost cards, transform into a 3/3 copy of a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass