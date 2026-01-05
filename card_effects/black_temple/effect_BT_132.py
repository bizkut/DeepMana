"""Effect for Ironbark (BT_132).

Card Text: Give a minion +1/+3 and <b>Taunt</b>.
Costs (0) if you have at least 7 Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1