"""Effect for Whelp Bonker (ONY_003).

Card Text: <b>Frenzy and Honorable Kill:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)