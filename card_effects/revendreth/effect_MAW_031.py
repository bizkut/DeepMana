"""Effect for Afterlife Attendant (MAW_031).

Card Text: Your <b>Infuse</b> cards also <b>Infuse</b> while in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass