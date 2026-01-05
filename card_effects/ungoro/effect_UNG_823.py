"""Effect for Envenom Weapon (UNG_823).

Card Text: Give your weapon <b>Poisonous</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1