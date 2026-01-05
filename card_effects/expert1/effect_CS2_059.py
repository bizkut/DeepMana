"""Effect for Blood Imp (CS2_059).

Card Text: [x]  <b>Stealth</b>. At the end of your  
turn, give another random
 friendly minion +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)