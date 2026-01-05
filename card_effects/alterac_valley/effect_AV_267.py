"""Effect for Caria Felsoul (AV_267).

Card Text: <b>Battlecry:</b> Transform into a 6/6 copy of a Demon in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass