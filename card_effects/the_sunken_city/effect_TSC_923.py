"""Effect for Bioluminescence (TSC_923).

Card Text: Give your minions
<b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1