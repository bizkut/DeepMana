"""Effect for Dirty Tricks (BT_709).

Card Text: [x]<b>Secret:</b> After your
opponent casts a spell,
draw 2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)