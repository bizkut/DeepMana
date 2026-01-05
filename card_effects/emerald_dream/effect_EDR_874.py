"""Effect for Stellar Balance (EDR_874).

Card Text: Get a Moonfire and
a Starfire. Give them <b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1