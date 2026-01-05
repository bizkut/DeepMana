"""Effect for Wardruid Loti (TRL_343).

Card Text: <b>Choose One - </b>Transform into one of Loti's four dinosaur forms.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass