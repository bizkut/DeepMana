"""Effect for Good Vibrations (ETC_373b).

Card Text: Give your minions +2/+4 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
