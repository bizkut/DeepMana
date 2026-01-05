"""Effect for Dr. Boom, Mad Genius (BOT_238).

Card Text: <b>Battlecry:</b> For the rest of the game, your Mechs have <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass