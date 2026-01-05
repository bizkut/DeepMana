"""Effect for Barkshield Sentinel (EDR_470).

Card Text: [x]<b>Taunt</b>
After you use your Hero
Power, gain +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)