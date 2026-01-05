"""Effect for The Countess (REV_951).

Card Text: [x]<b>Battlecry:</b> If your deck 
has no Neutral cards, add 
3 <b>Legendary </b>Invitations 
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass