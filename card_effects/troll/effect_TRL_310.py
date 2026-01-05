"""Effect for Elemental Evocation (TRL_310).

Card Text: The next Elemental you play this turn costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass