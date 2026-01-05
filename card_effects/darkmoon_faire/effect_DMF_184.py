"""Effect for Fairground Fool (DMF_184).

Card Text: <b>Taunt</b>
<b>Corrupt:</b> Gain +4 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)