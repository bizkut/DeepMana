"""Effect for To the Front! (AV_119).

Card Text: Your minions cost (2) less this turn <i>(but not less than 1)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass