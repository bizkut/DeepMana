"""Effect for Brilliant Macaw (DED_509).

Card Text: <b>Battlecry:</b> Repeat the last <b>Battlecry</b> you played.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass