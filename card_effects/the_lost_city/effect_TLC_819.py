"""Effect for Gladesong Siren (TLC_819).

Card Text: <b>Lifesteal</b>
Costs (1) if you've
played a Holy and Shadow spell this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass