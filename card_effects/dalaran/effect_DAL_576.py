"""Effect for Kirin Tor Tricaster (DAL_576).

Card Text: <b>Spell Damage +3</b>
Your spells cost (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3