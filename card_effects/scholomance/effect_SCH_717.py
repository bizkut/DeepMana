"""Effect for Keymaster Alabaster (SCH_717).

Card Text: [x]Whenever your opponent
 draws a card, add a copy to 
 your hand that costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)