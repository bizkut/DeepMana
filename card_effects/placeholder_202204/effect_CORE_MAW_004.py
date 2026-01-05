"""Effect for Soul Seeker (CORE_MAW_004).

Card Text: <b>Battlecry:</b> Swap this with a random minion from your opponent's deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass