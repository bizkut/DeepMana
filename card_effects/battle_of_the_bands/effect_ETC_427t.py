"""Effect for Dissonant Metal (ETC_427t).

Card Text: [x]Give 2 random minions in your hand +4/+4. <i>(Swaps each turn.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
