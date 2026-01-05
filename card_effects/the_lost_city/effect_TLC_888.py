"""Effect for Cloud Serpent (TLC_888).

Card Text: [x]<b>Battlecry:</b> Get a copy
of another Elemental or
Dragon in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass