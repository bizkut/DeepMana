"""Effect for Generous Mummy (ULD_214).

Card Text: <b>Reborn</b>
Your opponent's cards cost (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass