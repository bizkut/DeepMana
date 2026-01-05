"""Effect for Serpentbloom (WC_007).

Card Text: Give a friendly
Beast <b>Poisonous</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1