"""Effect for Desperate Measures (DAL_141).

Card Text: <b>Twinspell</b>
Cast a random Paladin <b>Secret</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass