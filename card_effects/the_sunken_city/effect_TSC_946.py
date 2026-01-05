"""Effect for Urchin Spines (TSC_946).

Card Text: Your spells this turn are <b>Poisonous</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass