"""Effect for Kiri, Chosen of Elune (CORE_DMF_733).

Card Text: <b>Battlecry:</b> Add a Solar Eclipse and Lunar Eclipse to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass