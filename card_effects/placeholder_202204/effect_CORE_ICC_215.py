"""Effect for Archbishop Benedictus (CORE_ICC_215).

Card Text: <b>Battlecry:</b> Shuffle a copy of your opponent's deck into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass