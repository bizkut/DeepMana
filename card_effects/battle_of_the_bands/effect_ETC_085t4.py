"""Effect for Movement of Gluttony (ETC_085t4).

Card Text: Give a random minion in your hand, deck, and battlefield +6/+6.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
