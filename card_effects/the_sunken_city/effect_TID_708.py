"""Effect for Polymorph: Jellyfish (TID_708).

Card Text: Transform a minion
into a 4/1 Jellyfish with <b>Spell Damage +2</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4