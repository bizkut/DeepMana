"""Effect for Velen's Chosen (GVG_010).

Card Text: Give a minion +2/+4 and <b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2