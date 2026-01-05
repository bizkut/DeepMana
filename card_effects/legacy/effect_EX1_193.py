"""Effect for Psychic Conjurer (EX1_193).

Card Text: <b>Battlecry:</b> Copy a card in your opponent’s deck and add it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass