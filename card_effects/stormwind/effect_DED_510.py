"""Effect for Edwin, Defias Kingpin (DED_510).

Card Text: [x]<b>Battlecry:</b> Draw a card. If you
play it this turn, gain +2/+2
and repeat this effect.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)