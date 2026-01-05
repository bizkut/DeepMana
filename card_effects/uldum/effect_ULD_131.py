"""Effect for Untapped Potential (ULD_131).

Card Text: [x]<b>Quest:</b> End 4 turns
with any unspent Mana.
<b>Reward:</b> Ossirian Tear.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass