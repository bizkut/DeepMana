"""Effect for Dire Frenzy (GIL_828).

Card Text: Give a Beast +3/+3. Shuffle 3 copies into your deck with +3/+3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3