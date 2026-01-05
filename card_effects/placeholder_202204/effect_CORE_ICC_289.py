"""Effect for Moorabi (CORE_ICC_289).

Card Text: Whenever another minion is <b>Frozen</b>, add a copy of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass