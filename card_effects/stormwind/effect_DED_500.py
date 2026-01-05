"""Effect for Wealth Redistributor (DED_500).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> Swap the
Attack of the highest and
lowest Attack minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass