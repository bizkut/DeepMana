"""Effect for Plagiarize (SCH_706).

Card Text: <b>Secret:</b> At the end of your opponent's turn, add copies of the cards they played to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass