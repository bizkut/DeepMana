"""Effect for Escape the Underfel (TLC_446).

Card Text: <b>Quest:</b> Play 6 <b>Temporary</b> cards. <b>Reward:</b> Underfel Rift.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass