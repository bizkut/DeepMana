"""Effect for Gift of the Wild (EX1_183).

Card Text: Give your minions +2/+2 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2