"""Effect for Anubisath Defender (ULD_138).

Card Text: <b>Taunt</b>. Costs (0) if you've cast a spell that costs (5) or more this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass