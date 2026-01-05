"""Effect for Gnash (CORE_ICC_079).

Card Text: Give your hero +3 Attack this turn. Gain 3 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3