"""Effect for Aviana, Elune's Chosen (EDR_895).

Card Text: [x]<b>Battlecry:</b> Start a three
turn lunar cycle. When the
Full Moon rises, your cards
cost (1) this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass